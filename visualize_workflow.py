from src.graph.builder import build_graph
from src.model import LLM
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)

# Build và compile graph
graph = build_graph(llm)
workflow = graph.compile()

# Mermaid diagram
try:
    mermaid = workflow.get_graph().draw_mermaid()
    print("\nMermaid code:")
    print(mermaid)
except Exception as e:
    print(f"Mermaid error: {e}")