from typing import Literal
from langgraph.graph import  END, START, StateGraph
from pydantic import BaseModel, Field
from src.model import LLM
from .state import ContentState
from src.nodes import analyze_topic, generate_outline, research_info,write_content , review_content
class Feedback(BaseModel):
    grade: Literal["yes", "no"] = Field(
        description="quyết định xem bài viết có chất lượng hay không",
    )
    feedback: str = Field(
        description="nhận xét chi tiết về bài viết dựa trên chất lượng nội dung",
    )
    issues: str = Field(
        description="vấn đề cần sửa trong bài viết",
    )
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
    def review_content_node(state: ContentState) -> ContentState:
        return review_content(state=state, api_llm=llm)
    def call_elevator(state: ContentState):
        if state.get("count_evaluate", 0) >= 1:
            return {"yes_no": "yes"}
        else:
            content = state["draft_content"]
            evaluator = llm.llm.with_structured_output(Feedback)
            prompt = f"""Đánh giá chất lượng bài viết sau dựa trên 4 tiêu chí (mỗi tiêu chí 0-25 điểm):

            BÀI VIẾT:
            {content}

            TIÊU CHÍ ĐÁNH GIÁ:
            1. Nội dung liên quan (Relevance): Bài có trả lời đúng chủ đề không?
            2. Cấu trúc rõ ràng (Structure): Bài có intro, body, conclusion rõ ràng không?
            3. Ngữ pháp & chính tả (Grammar): Có lỗi chính tả, ngữ pháp không?
            4. Sâu sắc & chi tiết (Depth): Có đủ thông tin, ví dụ, chi tiết không?

            Dựa vào đánh giá, hãy trả lời:
            - grade: "yes" nếu bài viết đạt chất lượng (tổng điểm >= 60), "no" nếu cần sửa
            - feedback: Nhận xét chi tiết về các điểm mạnh và yếu của bài viết (ít nhất 50 từ)
            - issues: Liệt kê cụ thể 3-5 vấn đề chính cần sửa"""
            
            response = evaluator.invoke(prompt)
            return {
                "yes_no": response.grade,
                "quality_feedback": response.feedback,
                "issues": response.issues,
                "count_evaluate": state.get("count_evaluate", 0) + 1
            }
    def route_decision(state: ContentState) -> str:
        if state["yes_no"] == "yes":
            return "yes"
        else:
            return "no"
    # Thêm các nút vào đồ thị
    graph.add_node("analyze_topic",analyze_topic_node)
    graph.add_node("research_info", research_info_node)
    graph.add_node("generate_outline", generate_outline_node)
    graph.add_node("write_content", write_content_node)
    graph.add_node("call_elevator", call_elevator)
    graph.add_node("review_content", review_content_node)
    # Kết nối các nút với nhau
    graph.add_edge(START, "analyze_topic")
    graph.add_edge("analyze_topic", "research_info")
    graph.add_edge("analyze_topic", "generate_outline")
    graph.add_edge("generate_outline","write_content")
    graph.add_edge("research_info","write_content")
    graph.add_edge("write_content", "call_elevator")
    graph.add_conditional_edges("call_elevator", route_decision, {
        "yes": "review_content",
        "no": "review_content"
    })
    graph.add_edge("review_content", END)
    
    return graph

