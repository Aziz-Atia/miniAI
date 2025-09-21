from google import genai
import sys
import os
from dotenv import load_dotenv
from google.genai import types


def main():
    print("Hello from miniai!")


if __name__ == "__main__":
    main()
load_dotenv()
inputContents = sys.argv[1]
client = genai.Client(api_key= os.environ.get("GEMINI_API_KEY")) #except writing api_key=api_key, writing this way
messages = [
    types.Content(role="user", parts=[types.Part(text=inputContents)]),
]
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
print(response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens: ", response.usage_metadata.candidates_token_count)