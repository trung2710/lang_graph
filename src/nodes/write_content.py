from src.graph.state  import ContentState
from src.model import LLM
# Node 4: Write Content
def write_content(state: ContentState, api_llm: LLM) -> ContentState:
    """Viết nội dung chi tiết dựa trên outline và research info"""
    topic = state["topic"]
    outline = state["outline"]
    research = state["research_info"]
    
    prompt = f"""Viết bài viết ngắn gọn dựa trên:
    
    Chủ đề: {topic}
    
    Outline:
    {outline}
    
    Thông tin tham khảo:
    {research}
    
    Yêu cầu:
    - Viết ngắn gọn, súc tích
    - Tuân theo outline
    - Sử dụng thông tin từ research
    - Độ dài: 200-300 từ (KHÔNG vượt quá)
    - Viết bằng tiếng Việt, tự nhiên"""
    llm=api_llm.llm
    response = llm.invoke(prompt)
    # state["draft_content"] = response.content
    return {"draft_content": response.content}