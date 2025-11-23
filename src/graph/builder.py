from langgraph.graph import  END, START, StateGraph
from src.model import LLM
from dotenv import load_dotenv
import os
from .state import ContentState
from src.nodes.analyze_topic import analyze_topic
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
api_llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)
llm=api_llm.llm
def build_graph():
    graph=StateGraph(ContentState)
    # Thêm các nút vào đồ thị
    graph.add_node("analyze_topic", analyze_topic)


    # Kết nối các nút với nhau
    graph.add_edge(START, "analyze_topic")
    graph.add_edge("analyze_topic", END)
    
    return graph

