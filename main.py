from deepagents import create_deep_agent



@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="qwen3:9b",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "what is the weather in Prague"}
    ]
})

print(result)