from openai import OpenAI


def main():
    # Point the OpenAI client at Ollama's OpenAI-compatible endpoint
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # any non-empty string; Ollama ignores it
    )

    resp = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain LBW in cricket in 2 sentences."},
        ],
        temperature=0.3,
        max_tokens=150,
    )

    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
