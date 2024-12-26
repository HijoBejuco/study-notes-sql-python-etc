
# Ensure credentials are configured
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

SOURCE = """
    Old Ship Saloon 2023 quarterly revenue numbers:
    Q1: $174782.38
    Q2: $467372.38
    Q3: $474773.38
    Q4: $389289.23
"""
QUESTION = "What is the revenue of Old Ship Saloon in first 2 Q 2023?"
VERTEXAI_MODEL = "gemini-1.5-flash"

def main():
    chat_model = ChatVertexAI(model=VERTEXAI_MODEL)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a finantial advisor. So analyze this: \n {information}"),
        ("human", "{question}")
    ])

    # Constructing the chain
    chain = prompt | chat_model | StrOutputParser()

    result = chain.invoke({
        "information": SOURCE,
         "question": QUESTION
    })
    
    print("\n" + result)

if __name__ == "__main__":
    main()