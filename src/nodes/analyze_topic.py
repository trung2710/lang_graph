from src.graph.state import ContentState
from src.model import LLM
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
api_llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)
llm=api_llm.llm
def analyze_topic(state: ContentState) -> ContentState:
    """Phân tích chủ đề, trích xuất từ khóa, xác định loại content"""
    topic = state["topic"]
    
    prompt = f"""Phân tích chủ đề sau: "{topic}"
    
    Hãy:
    1. Xác định loại content phù hợp (blog post, essay, article, guide, etc.)
    2. Trích xuất 5-7 từ khóa chính
    
    Trả về theo format:
    CONTENT_TYPE: [loại]
    KEYWORDS: [từ khóa, cách nhau bởi dấu phẩy]"""
    
    response = llm.invoke(prompt)
    content = response.content
    
    lines = content.split('\n')
    content_type = "blog post"
    keywords = []
    
    for line in lines:
        if line.startswith("CONTENT_TYPE:"):
            content_type = line.replace("CONTENT_TYPE:", "").strip()
        elif line.startswith("KEYWORDS:"):
            keywords_str = line.replace("KEYWORDS:", "").strip()
            keywords = [k.strip() for k in keywords_str.split(",")]
    
    state["content_type"] = content_type
    state["keywords"] = keywords
    return state