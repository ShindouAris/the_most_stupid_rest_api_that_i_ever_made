import requests

url = "http://localhost:8000/generate_audio"

payload = {
    "request_id": "123",
    "text": "Hello, my name is John",
    "language": "en",
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Audio file generated successfully")
    with open("response.mp3", "wb") as file:
        file.write(response.content)

else:
    print("Failed to generate audio file")
    print(response.text)