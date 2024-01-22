import openai
import json
import requests
import os
import tkinter as tk


def process_image_with_prompt(base64_image, prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 250
    }

    print("Sending request to OpenAI...")
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()

    if response.status_code != 200:
        print(f"Error from OpenAI: {response_json}")
        return "Error in processing the image"

    if 'choices' in response_json and response_json['choices']:
        content = response_json['choices'][0].get('message', {}).get('content', 'No response content')
        print("Received response from OpenAI")
        return content
    else:
        print("No valid response received")
        return "No valid response received"


def process_text_with_prompt(text, prompt):
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt + " " + text},
        ],
        max_tokens=300
    )
    return client.choices[0].message.content

# The existing functions can be retained or modified according to your specific needs.
