
# LangChain Agent Demo

This project demonstrates the integration of LangChain agents to perform task automation. The example is based on calculating mathematical expressions using a calculator tool. It uses the LangChain framework to initialize and execute the agent with OpenAI's language model for reasoning and interacting with tools.

---
![Screenshot](https://github.com/DilshanaRanawake/LangChain-Agent-Demo/blob/main/Screenshot/Screenshot%202025-05-06%20223103.png)

## Table of Contents

- [Setup](#setup)
- [Learning Notes](#learning-notes)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Tools Summary](#tools-summary)

## Setup

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/LangChain-Agent-Demo.git
   cd LangChain-Agent-Demo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv agent-env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     agent-env\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     source agent-env/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```
   (On Windows, use `set` instead of `export`)

6. **Run the application:**
   ```bash
   python agent_app.py
   ```

## Learning Notes

In this project, I learned how to:

1. **Set up LangChain Agents:** Understanding how LangChain agents are initialized and executed.
2. **Interact with LLM (Large Language Models):** Using OpenAI's language model to handle reasoning and decision-making for the agent.
3. **Handle tool calls:** Demonstrating how an agent can call external tools (e.g., a calculator) to perform tasks.
4. **Understand deprecation warnings:** Acknowledging LangChain's move towards LangGraph for agent implementations, and learning how to work with both tools.

## Example Usage

When you run the agent, it will process a simple mathematical question:

```bash
What is 5 * (7 + 2)?
```

The agent will use a tool (Calculator) to evaluate the expression, returning:

```bash
Final Answer: 45
```

## Project Structure

- `agent_app.py`: Main script to run the agent.
- `requirements.txt`: Dependencies for the project (e.g., LangChain, OpenAI).
- `README.md`: Documentation for the project.
- `tools/`: Contains custom tool implementations for the agent (e.g., Calculator).


## Tools Summary

| Tool Name   | Purpose               | Description                                                |
|-------------|-----------------------|------------------------------------------------------------|
| Calculator | Math Operations       | Performs basic arithmetic operations such as addition, subtraction, multiplication, and division. |

---
