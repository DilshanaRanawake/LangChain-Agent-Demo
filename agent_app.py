import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType

# Load .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

# Setup LLM
llm = ChatOpenAI(
    api_key=api_key,
    model="openai/gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1"
)


# Dummy tool just so the agent can run
def calc_tool(text):
    return str(eval(text))

tools = [
    Tool(
        name="Calculator",
        func=calc_tool,
        description="Does math like '5 * (7 + 2)'"
    )
]

# Init agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run it
query = "What is 5 * (7 + 2)?"
response = agent.invoke({"input": query})
print("Response:", response)
