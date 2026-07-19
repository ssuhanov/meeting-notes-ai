from openai import OpenAI

client = OpenAI(api_key="")

print("Available models:")
for model in client.models.list():
    print(model.id)

current_model = "gpt-5.5"
prompt = "Tell me how can I become an AI Engineer"
print("Prompt: " + prompt)
response = client.chat.completions.create(
    model=current_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
