from src.graph.state import ContentState
from src.model import LLM
# Node 5: Review & Polish
def review_content(state: ContentState, api_llm : LLM) -> ContentState:
    """Review, sửa lỗi, format lại nội dung"""
    draft = state["draft_content"]
    
    prompt = f"""Review và cải thiện bài viết sau:
    
    {draft}
    
    Hãy:
    1. Kiểm tra lỗi chính tả, ngữ pháp
    2. Cải thiện flow và readability
    3. Thêm emphasis cho key points (dùng **)
    4. Thêm conclusion mạnh
    
    Trả về bài viết đã được cải thiện."""
    llm=api_llm.llm
    response = llm.invoke(prompt)

    return {"final_content": response.content}