from src.graph.state import ContentState
from src.model import LLM
# Node 3: Generate Outline (song song)
def generate_outline(state: ContentState, api_llm: LLM) -> ContentState:
    """Tạo outline/cấu trúc cho bài viết"""
    topic = state["topic"]
    content_type = state["content_type"]
    
    llm = api_llm.llm
    prompt = f"""Tạo outline chi tiết cho một {content_type} về '{topic}'
    
    Outline phải có:
    1. Introduction (hook + thesis)
    2. 3-4 main sections
    3. Conclusion
    
    Mỗi section có 2-3 điểm chính. Format rõ ràng với heading và sub-points."""
    
    response = llm.invoke(prompt)

    return {"outline": response.content}