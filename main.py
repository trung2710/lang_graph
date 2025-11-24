from src.model import LLM
from dotenv import load_dotenv
import os
from src.graph import build_graph
from src.graph import ContentState
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)

def main():
    print("Hello from lang-graph!")
    # Xây dựng graph
    graph = build_graph(llm)
    # Khởi tạo trạng thái ban đầu
    content=input("Nhập chủ đề bạn muốn viết về: ")
    # Giới thiệu sơ lược về langgraph và cách build 1 workflow đơn giản
    initial_state: ContentState = {
        "topic": content,
        "content_type": None,
        "keywords": None,
        "research_info": None,
        "outline": None,
        "draft_content": None,
        "final_content": None,
    }
    # Thực thi graph với trạng thái ban đầu
    # Nó trả về một đối tượng LangGraph Runnable (thường được đặt tên là app hoặc agent) 
    #để có thể gọi bằng .invoke() hoặc .stream().
    workflow=graph.compile()
    state=workflow.invoke(initial_state)
    print("content State:", state["content_type"])
    print("keywords:", state["keywords"])
    print("research info:", state["research_info"])
    print("outline:", state["outline"])
    print("draft content:", state["draft_content"])
    print("final content:", state["final_content"])

if __name__ == "__main__":
    main()
