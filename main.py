from ollama import chat
import sys
from langfuse import Langfuse

stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Who is pachamama'}],
    stream=True,
)

if __name__ == '__main__':
    try:
        if sys.argv[1]:
            print("...")
    except IndexError:
        print('Chat mode: llama3.2')
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)