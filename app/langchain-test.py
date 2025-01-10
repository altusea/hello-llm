from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os


def main():
    # read api key from '.deepseek' text file in home directory
    os.environ["DEEPSEEK_API_KEY"] = (
        open(os.path.expanduser("~/.deepseek"), "r").read().strip()
    )

    # Initialize the LLM
    llm = ChatOpenAI(
        base_url="https://api.deepseek.com/v1",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=1.3,
        model="deepseek-chat",
    )

    # Create conversation chain with memory
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)

    print("LangChain Demo - Simple Chatbot\n")
    print("Type 'exit' to end the conversation\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = conversation.predict(input=user_input)
        print(f"AI: {response}")


if __name__ == "__main__":
    main()
