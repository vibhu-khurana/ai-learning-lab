from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "Generate a caption for this image in about 50 words?"},
            {
                "type": "input_image",
                "image_url": "https://images.pexels.com/photos/4145153/pexels-photo-4145153.jpeg",
            },
        ],
    }],
)

print("Response: ", response.output_text)