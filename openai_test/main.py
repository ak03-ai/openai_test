# This is a sample Python script.

import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")

question = input("Type your question?\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  message=[
    {"role":"system","content": "You are a helpful assistant. Answer the given question."},
    {"role":"user","content":question}
  ]
)
print(completion.choices[0].message.content)