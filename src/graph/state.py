from typing import TypedDict, Optional, List, Annotated
from langgraph.graph.message import add_messages
from ..model import LLM
from langchain_core.tools import StructuredTool

class State(TypedDict):
    tools: Optional[List[StructuredTool]]
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