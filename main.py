from deepagents import create_deep_agent



agent = create_deep_agent(
    model="qwen3:9b",
    system_prompt="You are a helpful assistant",
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "How are you?"}
    ]
})

print(result)