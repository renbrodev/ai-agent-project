import os 
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types 

def main():

    # need this to get the stuff from our .env file
    load_dotenv()
    
    # need this to talk to gemini
    api_key = os.environ.get("GEMINI_API_KEY")

    # being used currently in a similar manner to Scanner in Java (ie for accepting user input). has other explorable uses though...
    parser = argparse.ArgumentParser(description="'Chatbot'")
    parser.add_argument("user_prompt", type=str, help="User Prompt: ")
    args = parser.parse_args()

    if api_key is None:
        raise RuntimeError("Environment variable not found...")


    client = genai.Client(api_key=api_key)

    # test query
    # query = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    
    # direct user input query. model treats as in a vacuum so follow up questions wont be understood as part of a conversation
    # query = args.user_prompt

    # retrieve response from a specific model of gemini. this version could not do run on conversations
    # response = client.models.generate_content(model='gemini-2.5-flash', contents=query)

    # messages will track the conversation as opposed to query which only tracked an individual question
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    # collect info so we can track / work out costs as we talk to this thing
    usage_metadata = response.usage_metadata

    # don't leave the user hanging if something went wrong
    if usage_metadata is None:
        raise RuntimeError("No usage metadata in response - API may have returned an unexpected result")
    
    # tokens are the metric used to figure out the size of responses and queries which affects costs. something like 4ish characters per token.
    prompt_token_count = usage_metadata.prompt_token_count
    candidates_token_count = usage_metadata.candidates_token_count

    # print(f"User prompt: {query}")
    print(f"User prompt: {messages}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()