from src.graph.state  import ContentState
from src.model import LLM
# Node 4: Write Content
def write_content(state: ContentState, api_llm: LLM) -> ContentState:
    if state.get("yes_no") == "no":
        """Viết lại nội dung dựa trên feedback và issues"""
        topic = state["topic"]
        outline = state["outline"]
        research = state["research_info"]
        issues = state["issues"]
        feedback = state["quality_feedback"]
        prompt = f"""Dựa trên các thông tin sau, viết lại bài viết để cải thiện chất lượng:
        Chủ đề: {topic}
        Outline:
        {outline}
        Thông tin tham khảo:
        {research}
        Nhận xét về chất lượng bài viết:
        {feedback}
        Vấn đề cần sửa:
        {issues}
        Yêu cầu:
        - Viết ngắn gọn, súc tích
        -Sửa các vấn đề được chỉ ra
        - Tuân theo outline
        - Sử dụng thông tin từ research
        - Độ dài: 200-300 từ (KHÔNG vượt quá)
        - Viết bằng tiếng Việt, tự nhiên
        """
        llm = api_llm.llm
        response = llm.invoke(prompt)
        return {"draft_content": response.content}
    else:
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
        llm = api_llm.llm
        response = llm.invoke(prompt)
        return {"draft_content": response.content}