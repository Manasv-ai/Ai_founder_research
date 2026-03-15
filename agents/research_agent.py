from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()

def summarize_company(info):

    prompt = f"""
    Summarize this startup in 3 lines.

    {info}
    """

    return llm.predict(prompt)