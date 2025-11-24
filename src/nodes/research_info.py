from src.graph.state import ContentState
from src.model import LLM

# Node 2: Research & Gather Info (song song)
def research_info(state: ContentState, api_llm: LLM) -> ContentState:
    """Tìm thông tin và context liên quan đến chủ đề"""
    topic = state["topic"]
    keywords = state["keywords"]
    keywords_str = ", ".join(keywords[:3])
    
    prompt = f"""Về chủ đề '{topic}' với từ khóa: {keywords_str}
    
    Hãy cung cấp:
    1. Định nghĩa và giới thiệu
    2. Các sự kiện/ngữ cảnh quan trọng
    3. Các khía cạnh chính cần đề cập
    
    Viết gọn, có cấu trúc rõ ràng."""
    llm=api_llm.llm
    response = llm.invoke(prompt)

    return {"research_info": response.content} 