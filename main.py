from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=ChatOllama(model="qwen3:8b"),
    tools=[get_weather],
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "what is the weather in Prague"}
    ]
})

print(result)