####################################
#
# To run first install following in your Python environment:
#
# $pip install boto3
# $pip install langchain
#
########################


import boto3

from langchain.chat_models import BedrockChat

from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

modelId = 'anthropic.claude-v2'

chat = BedrockChat(model_id=modelId, region_name = 'us-west-2', model_kwargs={"temperature": 0.1})
#chat = BedrockChat(model_id=modelId, model_kwargs={"temperature": 0.1})

memory = ConversationBufferMemory(memory_key="messages", return_messages=True)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
        ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory
)

while True:
    content = input(">> ")
    
    result = chain({"content": content})
    
    print (result["text"])
    
    
    
    
