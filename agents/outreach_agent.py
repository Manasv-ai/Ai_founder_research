from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()

def generate_email(founder, company):

    prompt = f"""
    Write a short cold email.

    Founder: {founder}
    Company: {company}

    Keep it friendly and concise.
    """

    return llm.predict(prompt)