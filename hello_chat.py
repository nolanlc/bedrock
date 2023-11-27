import boto3

from langchain.chat_models import BedrockChat
from langchain.schema import HumanMessage

from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

modelId = 'anthropic.claude-v2'

chat = BedrockChat(model_id=modelId, region_name = 'us-west-2', model_kwargs={"temperature": 0.1})
#chat = BedrockChat(model_id=modelId, model_kwargs={"temperature": 0.1})

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
        ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt
)

while True:
    content = input(">> ")
    result = chain({"content": content})
    
    #print (result["text"])
