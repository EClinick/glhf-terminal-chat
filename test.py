import os
import openai
import dotenv


dotenv.load_dotenv()

def initialize_client():
    # Retrieve API key from environment variable
    api_key = os.getenv("GLHF_API_KEY")
    if not api_key:
        print("Error: GLHF_API_KEY environment variable not set.")
        return None

    # Set the API key and base URL
    openai.api_key = api_key
    openai.api_base = "https://glhf.chat/api/openai/v1"

    return openai

def fetch_models(client):
    try:
        models = openai.Model.list()
        print("Available Models:")
        for model in models['data']:
            print(f"- {model['id']}")
    except Exception as e:
        print(f"Error fetching models: {e}")

def main():
    client = initialize_client()
    if client:
        fetch_models(client)

if __name__ == "__main__":
    main()
