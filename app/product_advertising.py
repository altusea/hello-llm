import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# read api key from '.deepseek' text file in home directory
os.environ["DEEPSEEK_API_KEY"] = (
    open(os.path.expanduser("~/.deepseek"), "r").read().strip()
)


# 1. 设置LLM模型
llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=1.3,
    model="deepseek-chat",
)

# 2. 创建产品卖点生成模板
product_highlights_template = PromptTemplate(
    input_variables=["product_name", "features"],
    template="""
    你是一个专业的市场营销专家。请为以下产品生成3个主要卖点：
    产品名称：{product_name}
    产品特点：{features}
    
    要求：
    1. 每个卖点不超过20个字
    2. 突出产品独特优势
    3. 使用吸引人的营销语言
    
    卖点：
    """,
)

# 3. 创建宣传文案生成模板
ad_copy_template = PromptTemplate(
    input_variables=["product_name", "highlights"],
    template="""
    你是一个资深广告文案撰写人。请根据以下产品信息创作一段宣传文案：
    产品名称：{product_name}
    产品卖点：{highlights}
    
    要求：
    1. 文案长度在100-150字之间
    2. 包含情感诉求
    3. 突出产品价值主张
    
    宣传文案：
    """,
)

# 4. 构建chains
highlights_chain = LLMChain(llm=llm, prompt=product_highlights_template)
ad_copy_chain = LLMChain(llm=llm, prompt=ad_copy_template)

# 5. 示例调用
if __name__ == "__main__":
    product = {
        "name": "智能空气净化器",
        "features": "三重过滤系统，静音设计，智能空气质量监测",
    }

    # 生成卖点
    highlights = highlights_chain.run(
        {"product_name": product["name"], "features": product["features"]}
    )

    print("产品卖点：")
    print(highlights)

    # 生成宣传文案
    ad_copy = ad_copy_chain.run(
        {"product_name": product["name"], "highlights": highlights}
    )

    print("\n宣传文案：")
    print(ad_copy)
