from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model="llama3.2", messages=[
    {
        'role': 'user',
        'content': 'Who is pachamama?',
    },
])

print(response.message.content)