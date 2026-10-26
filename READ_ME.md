\# Ollama Tool-Using Agent



A beginner-friendly \*\*Agentic AI project\*\* built with Python and Ollama. This project demonstrates how a Large Language Model (LLM) can select and use tools to answer user queries.



\## Features



\- \*\*Local LLM:\*\* Uses Ollama to run an AI model locally.

\- \*\*Calculator Tool:\*\* Performs addition, subtraction, multiplication, and division.

\- \*\*Document Search:\*\* Searches local `.txt` files in the `documents/` directory.

\- \*\*Tool Calling:\*\* Allows the LLM to request Python functions when needed.

\- \*\*Agent Loop:\*\* Sends tool results back to the model to generate a final answer.

\- \*\*Multi-Step Tasks:\*\* Can combine document retrieval and calculations when the model selects the appropriate tools.



\## Technology Stack



\- Python

\- Ollama

\- Llama 3.2 3B (default model, if configured in `agent.py`)

\- Python Ollama library

\- PowerShell on Windows



\## Project Structure



```text

ollama-agent/

├── agent.py

├── documents/

│   └── company\_policy.txt

├── .gitignore

└── README.md

```



\## Requirements



\- Python 3.10 or compatible version

\- Ollama installed and running

\- A local Ollama model that supports tool calling



\## Installation and Setup



\### 1. Clone the repository



```powershell

git clone https://github.com/tasnimhere008/Ollama-Tool-Using-Agent.git

cd Ollama-Tool-Using-Agent

```



\### 2. Create and activate a virtual environment



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



\### 3. Install the dependency



```powershell

python -m pip install ollama

```



\### 4. Download the model



If your `agent.py` uses `llama3.2:3b`, run:



```powershell

ollama pull llama3.2:3b

```



Make sure the model name in `agent.py` matches an installed model.



\### 5. Run the agent



```powershell

python agent.py

```



Enter a question when prompted. Type `exit` to stop the program.



\## Example Tasks



\*\*Calculator\*\*



```text

Calculate 125 multiplied by 24.

```



\*\*Document Search\*\*



```text

What is the annual leave policy in the sample company document?

```



\*\*Multi-Step Task\*\*



```text

The annual leave allowance is 20 days and 5 days have been used. How many days remain?

```



The exact response depends on the available document content and the model's tool selection.



\## How It Works



1\. The user enters a question.

2\. The Python agent sends the question and available tool definitions to Ollama.

3\. The model may request a tool call.

4\. Python executes the selected tool.

5\. The tool result is returned to the model.

6\. The model produces a final answer or requests another tool, subject to the agent's iteration limit.



\## Current Limitations



\- Document search uses basic keyword matching.

\- Search results depend on document

