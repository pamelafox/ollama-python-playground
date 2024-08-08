import openai

MODEL_NAME = "phi3:mini"

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)


completion = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    max_tokens=500,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that makes lots of cat references and uses emojis."},
        {"role": "user", "content": "please write a novel about a hungry cat that wants tuna"},
    ],
    stream=True,
)

print("Response: ")
for event in completion:
    if event.choices:
        content = event.choices[0].delta.content
        print(content, end="", flush=True)