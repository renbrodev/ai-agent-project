import os 
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="'Chatbot'")
    parser.add_argument("user_prompt", type=str, help="User Prompt: ")
    args = parser.parse_args()

    if api_key is None:
        raise RuntimeError("Environment variable not found...")

    client = genai.Client(api_key=api_key)

    # test query
    # query = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=args
    )
    usage_metadata = response.usage_metadata

    if usage_metadata is None:
        raise RuntimeError("No usage metadata in response - API may have returned an unexpected result")
    
    prompt_token_count = usage_metadata.prompt_token_count
    candidates_token_count = usage_metadata.candidates_token_count

    print(f"User prompt: {args}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()