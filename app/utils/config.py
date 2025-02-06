import os


def read_api_key() -> str | None:
    try:
        with open(os.path.expanduser("~/.env"), "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("DEEPSEEK_API_KEY="):
                    return line.split("=", 1)[1]
            print("Error: DEEPSEEK_API_KEY not found in .env file.")
            return None
    except FileNotFoundError:
        print("Error: .env file not found. Please create a .env file with DEEPSEEK_API_KEY.")
        return None


def write_api_key_to_env(api_key: str):
    os.environ["DEEPSEEK_API_KEY"] = api_key
