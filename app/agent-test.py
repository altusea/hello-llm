from smolagents import CodeAgent, LiteLLMModel
from utils.config import read_api_key


def main():
    api_key = read_api_key()
    if api_key is None:
        return

    api_base = "https://api.deepseek.com/v1"
    model_id = "deepseek-chat"

    model = LiteLLMModel(model_id=model_id, api_base=api_base, api_key=api_key)
    agent = CodeAgent(tools=[], model=model, add_base_tools=True)

    agent.run(
        "Could you give me the 118th number in the Fibonacci sequence?",
    )


if __name__ == "__main__":
    main()
