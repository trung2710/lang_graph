from langgraph.graph import  END, START, StateGraph
from src.model import LLM
from .state import ContentState
from src.nodes import analyze_topic, generate_outline, research_info,write_content 

def build_graph(llm : LLM):
    graph=StateGraph(ContentState)
    
    #tao ham trung gian de truyen llm
    def analyze_topic_node(state: ContentState) -> ContentState:
        return analyze_topic(state=state, api_llm=llm)
    
    def research_info_node(state: ContentState) -> ContentState:
        return research_info(state=state, api_llm=llm)
    
    def generate_outline_node(state: ContentState) -> ContentState:
        return generate_outline(state=state, api_llm=llm)

    def write_content_node(state: ContentState) -> ContentState:
        return write_content(state=state, api_llm=llm)
    # Thêm các nút vào đồ thị
    graph.add_node("analyze_topic",analyze_topic_node)
    graph.add_node("research_info", research_info_node)
    graph.add_node("generate_outline", generate_outline_node)
    graph.add_node("write_content", write_content_node)
    # Kết nối các nút với nhau
    graph.add_edge(START, "analyze_topic")
    graph.add_edge("analyze_topic", "research_info")
    graph.add_edge("analyze_topic", "generate_outline")
    graph.add_edge("generate_outline","write_content")
    graph.add_edge("research_info","write_content")
    graph.add_edge("write_content", END)
    
    return graph

