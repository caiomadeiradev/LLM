import ollama
from ollama import chat
import uuid
import sys
from langfuse import Langfuse
import os
from dotenv import load_dotenv
import json

load_dotenv()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

def save_training_sample(user_input, response_text, correctness):
    with open("fine_tune_data.jsonl", "a", encoding="utf-8") as f:
        entry = {
            "prompt": user_input,
            "completion": " " + response_text.strip()
        }
        f.write(json.dumps(entry) + "\n")

def start_chat():
    stream = chat(
        model='llama3.2',
        stream=True,
    )
    return stream

def log_langfuse(input, response):
    langfuse.track_event(
        event="llama3.2_interaction",
        payload={"user_input": input, "model_response": response }
    )

if __name__ == '__main__':
    try:        

        trace_id = str(uuid.uuid4())
        trace = langfuse.trace(id=trace_id, name="ollama_trace")
        print(f"Trace ID {trace_id} and langfuse loaded")
        
        if sys.argv[1]:
            user_input = sys.argv[1]
            ollama_gen = trace.generation(name="llama3.2", input={"prompt": user_input})
            print("Trace generation done.")
            
            output = ollama.generate("llama3.2", prompt=user_input)
            print("OUTPUT:\n", output)
            
            response_text = output.get("response", "")
            prompt_eval_count = output.get("prompt_eval_count", 0)
            eval_count = output.get("eval_count", 0)
            total_duration = output.get("total_duration", 0)
            load_duration = output.get("load_duration", 0)
            
            # end langfuse generation trace
            ollama_gen.end(output=response_text, usage={
                "input":prompt_eval_count,
                "output":eval_count,
                "total_duration": total_duration,
                "load_duration": load_duration
            })
            
            correctness = float(input("Evaluate the anwser correction (0-1): "))
            langfuse.score(name="correctness", value=correctness, trace_id=trace_id,
                           data_type="NUMERIC", comment="Manual evaluation")
            
            save_training_sample(user_input, response_text, correctness)

            # updating trace with model's metadata
            trace.update(input=user_input, output=response_text, metadata={
                "model_name": "llama3.2",
                "eval_count":eval_count,
                "total_duration": total_duration,
                "prompt_eval_count": prompt_eval_count
            })
            
            print("Trace updated with extra metadata.")

            # Ensuring that data is sent
            langfuse.flush()
            print("Langfuse flushed.")

            # stream = chat(
            #     model='llama3.2',
            #     messages=[{'role': 'user', 'content': user_input }],
            #     stream=True,
            # )
            
            # # awnser response
            # response = ''
            # for chunk in stream:
            #     response += chunk['message']['content']
            # print(response, end='', flush=True)
            
            # # registrando o log interaction no langfuse
            # log_langfuse(user_input, response)

    except IndexError:
        print('Chat mode: llama3.2')
        stream = start_chat()
        
    # for chunk in stream:
    #     print(chunk['message']['content'], end='', flush=True)
    #     log_langfuse("user_input_placeholder", chunk['message']['content'])
