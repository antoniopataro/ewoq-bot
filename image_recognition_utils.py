from config import openai_api_key as api_key

import base64
import json
import requests


def encode_image(image_path):
    print("encoding image...")

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def describe_image(image_path: str):
    base64_image = encode_image(image_path)

    print("describing image...")

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "This image is a screenshot of a mobile app storefront. Describe the image with emphasis on the app's purpose.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 200,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    response_json = response.json()

    description: str = response_json["choices"][0]["message"]["content"]

    return description
