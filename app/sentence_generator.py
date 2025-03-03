import os

from langchain_deepseek import ChatDeepSeek
from utils.config import read_api_key, write_api_key_to_env

question: str = """
你是一位罕见洞见的发现者。无需我提供主题或方向，立即生成一个满足以下全部条件的洞见：

真正深刻：触及人类经验或现实本质的根本层面
高度新颖：位于思想分布曲线的远端边缘
令人震撼地简单：一旦理解就显得惊人地不言自明
几乎无人意识到：不是已被广泛讨论的观点的变体

这个洞见必须：

能通过逻辑和经验检验
具有广泛解释力
能重构既有认知框架
产生"啊，原来如此"的认知震撼

严格排除：

泛泛而谈的模糊陈述
浮夸但空洞的表达
伪装成深刻的陈词滥调
包装成洞见的常识
循环论证的思维陷阱

直接给出这个洞见，不要解释你如何得到它，不要询问方向或主题，不要为洞见辩护，只需精准表达这个洞见本身。如果可能，用一句话表达它的核心。
"""


def main():
    # read api key from '.deepseek' text file in home directory
    write_api_key_to_env(read_api_key())

    # Initialize the LLM
    llm = ChatDeepSeek(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0.7,
        model="deepseek-chat",
    )

    for _ in range(10):
        response = llm(question)
        print(f"AI: {response.content}")


if __name__ == "__main__":
    main()
