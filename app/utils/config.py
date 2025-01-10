import os


def read_api_key() -> str | None:
    try:
        with open(os.path.expanduser("~/.deepseek"), "r") as f:
            api_key = f.read().strip()
            return api_key
    except FileNotFoundError:
        print("Error: API key not found. Please set your API key in the .deepseek file.")
        return None


def write_api_key_to_env(api_key: str):
    os.environ["DEEPSEEK_API_KEY"] = api_key
