import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["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"]
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Trả lời đúng một câu: GitHub Action hoạt động!"
        }
    ]
)

print(response.choices[0].message.content)
