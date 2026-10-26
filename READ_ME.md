\# 🤖 Ollama Tool-Using Agent



A beginner-friendly \*\*Agentic AI project\*\* built with Python and Ollama. This project demonstrates how a Large Language Model (LLM) can understand user queries, select appropriate tools, execute tasks, and use tool results to generate a final answer.



The agent supports two tools:



\- 🧮 \*\*Calculator\*\* — performs mathematical calculations.

\- 📄 \*\*Document Search\*\* — searches local `.txt` files for relevant information.



Unlike a basic chatbot that only generates text, this project introduces a tool-using agent loop where the LLM can decide which tool to call based on the user's request.



* &#x20;Key Features



\- \*\*Local LLM Inference:\*\* Run an AI model locally using Ollama.

\- \*\*Automatic Tool Selection:\*\* The LLM decides whether to use the calculator or document search.

\- \*\*Mathematical Calculations:\*\* Supports addition, subtraction, multiplication, and division.

\- \*\*Local Document Search:\*\* Searches text files stored in the `documents/` directory.

\- \*\*Multi-Step Reasoning:\*\* Can retrieve information from a document and then perform a calculation using that information.

\- \*\*Tool Execution Feedback:\*\* Displays tool calls and their results in the terminal.

\- \*\*Bounded Agent Loop:\*\* Limits the number of tool-calling rounds to avoid endless execution.

\- \*\*Beginner-Friendly Architecture:\*\* Uses Python and Ollama without LangChain or MCP.



* &#x20;Project Objective



The goal is to understand the core concepts of Agentic AI by building a practical tool-using agent from scratch.



Through this project, we explore how an LLM interacts with external Python functions, receives their results, and continues processing until it can provide a final response.



* &#x20;Architecture



```text

&#x20;            User Query

&#x20;                |

&#x20;                v

&#x20;         Python Agent Loop

&#x20;                |

&#x20;                v

&#x20;          Local LLM

&#x20;            Ollama

&#x20;                |

&#x20;         Selects a Tool

&#x20;                |

&#x20;         +------+------+

&#x20;         |             |

&#x20;         v             v

&#x20;     Calculator   Document Search

&#x20;         |             |

&#x20;         v             v

&#x20;     Calculation   Local .txt Files

&#x20;         |             |

&#x20;         +------+------+

&#x20;                |

&#x20;                v

&#x20;         Tool Result

&#x20;                |

&#x20;                v

&#x20;         LLM Processes

&#x20;          the Result

&#x20;                |

&#x20;                v

&#x20;          Final Answer

```



\### How It Works



1\. The user submits a question through the terminal.

2\. The Python agent sends the conversation and available tool definitions to the local LLM.

3\. The LLM determines whether a tool is required and requests a tool call when appropriate.

4\. Python executes the selected function using the supplied arguments.

5\. The tool result is added to the conversation.

6\. The LLM processes the result and either requests another tool or generates the final answer.

7\. The agent stops when a final response is received or the maximum number of tool rounds is reached.



* Technology Stack



| Technology            | Purpose                                      |

| --------------------- | -------------------------------------------- |

| Python                | Agent logic and tool execution               |

| Ollama                | Running the LLM locally                      |

| Llama 3.2 3B          | Default model configured in the example code |

| Python Ollama Library | Communication with the Ollama API            |

| pathlib               | Local document and file handling             |

| PowerShell            | Running the project on Windows               |



\*\*Note:\*\* The configured model must be available in your local Ollama installation. You can change the model name in `agent.py` to another installed model that supports tool calling.



* &#x20;Project Structure



```text

ollama-agent/

│

├── agent.py

│   └── Main agent loop, tool definitions,

│       document search, and tool execution

│

├── documents/

│   └── company\_policy.txt

│       └── Sample company policy information

│

├── venv/

│   └── Python virtual environment

│

└── README.md

&#x20;   └── Project documentation

```



The `venv/` directory is created locally and should normally be excluded from Git using `.gitignore`.



\## ⚙️ Prerequisites



Before running the project, make sure you have:



\- Python 3.10 or a compatible Python version.

\- Ollama installed and running.

\- A local Ollama model that supports tool calling.

\- Windows PowerShell or another terminal.



* &#x20;Installation and Setup



\### 1. Clone the Repository



```bash

git clone https://github.com/YOUR\_USERNAME/ollama-agent.git

cd ollama-agent

```



Replace `YOUR\_USERNAME` with your GitHub username.



\### 2. Create a Virtual Environment



On Windows PowerShell:



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



\### 3. Install Dependencies



```powershell

python -m pip install ollama

```



\### 4. Start Ollama



Ensure Ollama is installed and running. Check the local API:



```powershell

Invoke-RestMethod http://127.0.0.1:11434/api/tags

```



\### 5. Download a Model



For example, to download Llama 3.2 3B:



```powershell

ollama pull llama3.2:3b

```



If you prefer another installed model, update the `MODEL` variable in `agent.py` accordingly.



\### 6. Run the Agent



```powershell

python agent.py

```



You should see a terminal prompt similar to:



```text

Ollama Tool-Using Agent

Type 'exit' to stop.



You:

```



Enter a question and type `exit` when you want to stop.



\## 💡 Example Use Cases



\### Example 1: Mathematical Calculation



\*\*Input\*\*



```text

Calculate 125 multiplied by 24.

```



\*\*Expected result\*\*



```text

\[Tool call] calculator: ...

\[Tool result] 3000



Agent: 125 multiplied by 24 is 3000.

```



The exact tool-call output and final wording may vary.



\### Example 2: Search Company Leave Policy



The sample `documents/company\_policy.txt` contains:



```text

Employees receive 20 days of annual leave per year.



Employees should request leave from their manager

before taking leave.

```



\*\*Input\*\*



```text

What is our company's annual leave policy?

```



\*\*Expected behavior\*\*



1\. The LLM selects `search\_documents`.

2\. Python searches the local text files.

3\. Relevant text is returned to the LLM.

4\. The agent summarizes the information in a response.



\### Example 3: Multi-Step Task



\*\*Input\*\*



```text

Our company provides 20 days of annual leave,

and I have taken 5 days. How many days remain?

```



\*\*Expected workflow\*\*



```text

User Query

&#x20;   |

&#x20;   v

Search Documents

&#x20;   |

&#x20;   v

Retrieve Annual Leave Information

&#x20;   |

&#x20;   v

Call Calculator: 20 - 5

&#x20;   |

&#x20;   v

Return Final Answer: 15 days

```



This example demonstrates how a tool-using agent can combine information retrieval with computation.



\*\*Important:\*\* The agent can perform this multi-step task only if the LLM correctly identifies the required tools and the document search retrieves the relevant information. The sample keyword search is simple and may miss relevant text.



* &#x20;Core Concepts Demonstrated



\*\*1. Large Language Model (LLM)\*\*



An LLM interprets natural-language questions, chooses tools, and generates responses.



\*\*2. Tool Calling\*\*



The model requests a predefined function with arguments. The Python application executes that function and returns the result.



\*\*3. Agent Loop\*\*



The application repeatedly sends the conversation to the LLM, executes requested tools, and processes results until the model returns a final answer or the iteration limit is reached.



\*\*4. Local AI\*\*



Ollama runs the model locally, so the application can use local inference without sending its prompts to a hosted LLM API through the normal inference path.



\*\*5. Multi-Step Task Execution\*\*



The agent can use the result of one tool call to inform a subsequent tool call.



* &#x20;Current Limitations



\- Document search uses basic keyword matching, not semantic search.

\- The project does not yet implement a complete Retrieval-Augmented Generation (RAG) pipeline.

\- Tool selection depends on the LLM's decisions.

\- Search quality depends on the content and formatting of local text files.

\- The agent has a fixed maximum number of tool-calling rounds.

\- The current tools are limited to calculations and local text search.

\- The project does not yet include persistent conversation memory, a web interface, or MCP integration.



* &#x20;Future Improvements



The project can be extended incrementally:



\-- Implement semantic search using embeddings.

\-- Build a RAG pipeline with document chunking and retrieval.

\-- Add source references to document-based answers.

\-- Implement a structured tool registry.

\-- Integrate MCP (Model Context Protocol) for standardized tool access.

\-- Add automated tests and logging.



* &#x20; Safety Considerations



\- Execute only explicitly registered tools.

\- Validate tool arguments before execution.

\- Handle division-by-zero and invalid operations.

\- Limit the number of agent iterations.

\- Treat retrieved document content as untrusted data.

\- Avoid exposing private documents or sensitive information in public repositories.

* &#x20;Learning Outcomes



After completing this project, you should understand:



\- How an LLM can select and call tools.

\- How Python executes tool requests.

\- How tool results are returned to an LLM.

\- How an agent performs multi-step tasks.

\- How local document search can be integrated with an AI agent.

\- How this foundation can be extended into RAG and MCP-based applications.





