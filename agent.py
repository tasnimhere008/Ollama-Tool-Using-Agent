
from pathlib import Path
from ollama import Client

client = Client(host="http://127.0.0.1:11434")
# Change to "qwen2.5:3b" if your model
# does not reliably make tool calls.
MODEL = "llama3.2:3b"

DOCUMENTS_DIR = Path(__file__).parent / "documents"


def calculator(a: float, b: float, operation: str) -> str:
    """Calculate two numbers using add, subtract, multiply, or divide.

    Args:
        a: First number.
        b: Second number.
        operation: One of add, subtract, multiply, divide.
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: cannot divide by zero."
        result = a / b
    else:
        return "Error: unsupported operation."

    return str(result)


def search_documents(query: str) -> str:
    """Search local text documents using keywords.

    Args:
        query: Words or phrase to search for.
    """
    if not DOCUMENTS_DIR.exists():
        return "Documents folder was not found."

    terms = set(query.lower().split())
    matches = []

    for path in DOCUMENTS_DIR.glob("*.txt"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        for paragraph in text.splitlines():
            paragraph = paragraph.strip()

            if not paragraph:
                continue

            words = set(paragraph.lower().split())
            score = len(terms & words)

            if score > 0:
                matches.append(
                    (score, path.name, paragraph)
                )

    matches.sort(key=lambda item: item[0], reverse=True)

    if not matches:
        return "No matching text found in the documents."

    results = [
        f"File: {filename} | Text: {paragraph}"
        for score, filename, paragraph in matches[:5]
    ]

    return "\n".join(results)


# Only these functions can be called by the agent.
TOOLS = [calculator, search_documents]

AVAILABLE_FUNCTIONS = {
    "calculator": calculator,
    "search_documents": search_documents,
}



def run_agent(question: str) -> None:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful local AI agent. "
                "Use calculator for mathematical calculations. "
                "Use search_documents for questions about local files. "
                "Do not invent document contents. "
                "If search returns no matching text, say so. "
                "After receiving tool results, answer the user clearly."
            ),
        },
        {"role": "user", "content": question},
    ]

    for step in range(5):
        response = client.chat(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )
        messages.append(response.message)

        tool_calls = response.message.tool_calls or []
        if not tool_calls:
            print("\nAgent:", response.message.content)
            return

        for call in tool_calls:
            name = call.function.name
            arguments = call.function.arguments
            print(f"\n[Tool call] {name}: {arguments}")

            function = AVAILABLE_FUNCTIONS.get(name)
            if function is None:
                result = "Error: tool is not allowed."
            else:
                try:
                    result = function(**arguments)
                except (TypeError, ValueError, OSError) as error:
                    result = f"Tool error: {error}"

            print("[Tool result]", result)
            messages.append({
                "role": "tool",
                "tool_name": name,
                "content": str(result),
            })

    print("\nAgent stopped: maximum tool rounds reached. Try a simpler question.")

if __name__ == "__main__":
    print("Ollama Tool-Using Agent")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            break

        if question:
            try:
                run_agent(question)
            except Exception as error:
                print("\nError connecting to Ollama or running the agent:", error)

