from deepagents import create_deep_agent
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3.5:9b",
    base_url="http://127.0.0.1:11434",
)

agent = create_deep_agent(
    model=llm,
    system_prompt="You are a helpful assistant",
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "How are you?"}
    ]
})

print(result)