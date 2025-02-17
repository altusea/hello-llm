import os
from typing import Dict, Optional

from dotenv import dotenv_values


def read_api_key() -> str | None:
    try:
        kv_dict: Dict[str, Optional[str]] = dotenv_values(os.path.expanduser("~/.env"))
        print(kv_dict.keys)

        v = kv_dict["DEEPSEEK_API_KEY"]
        if v is not None:
            return v
        print("Error: DEEPSEEK_API_KEY not found in .env file.")
        return None
    except FileNotFoundError:
        print(
            "Error: .env file not found. Please create a .env file with DEEPSEEK_API_KEY."
        )
        return None


def write_api_key_to_env(api_key: str):
    os.environ["DEEPSEEK_API_KEY"] = api_key


if __name__ == "__main__":
    kv_dict: Dict[str, Optional[str]] = dotenv_values(os.path.expanduser("~/.env"))
    for k, v in kv_dict.items():
        print(f"{k}: {v}")
