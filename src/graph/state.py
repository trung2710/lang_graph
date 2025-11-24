from typing import TypedDict, Optional, List, Annotated
from langgraph.graph.message import add_messages
from ..model import LLM
from langchain_core.tools import StructuredTool
import operator
class State(TypedDict):
    tools: Optional[List[StructuredTool]]
    # Annotated cho LangGraph biết cách xử lý hoặc cập nhật một key cụ thể trong State.
    # Qua việc kèm theo add_messages, LangGraph sẽ tự động thêm các messages vào trạng thái, thay vì ghi đè.
    messages: Annotated[List[dict], add_messages]
    answer: Optional[str]
    decison: Optional[str]


class ContentState(TypedDict):
    topic: Optional[str]  # Input chủ đề
    content_type: Optional[str]  # Loại content (blog, essay, etc.)
    keywords: Optional[list[str]]  # Từ khóa từ chủ đề
    research_info: Optional[str]  # Thông tin nghiên cứu
    outline: Optional[str]  # Outline bài viết
    draft_content: Optional[str]  # Nội dung draft
    final_content: Optional[str]  # Nội dung cuối cùng
    count_evaluate: Optional[int]  # Số lần viết lại
    yes_no: Optional[str]  # Đánh giá có đạt chất lượng hay không
    quality_feedback: Annotated[List[str], operator.add] = []
    issues: Optional[str]  # Vấn đề cần sửa trong bài viết