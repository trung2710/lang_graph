from src.model import LLM
from dotenv import load_dotenv
import os
from src.graph import build_graph
from src.graph import ContentState
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)
agent=llm.llm
def main():
    print("Hello from lang-graph!")
    # Xây dựng graph
    graph = build_graph()
    # Khởi tạo trạng thái ban đầu
    initial_state: ContentState = {
        "topic": "Lợi ích của việc đọc sách đối với sự phát triển cá nhân",
        "content_type": None,
        "keywords": None,
        "research_info": None,
        "outline": None,
        "draft_content": None,
        "final_content": None,
    }
    # Thực thi graph với trạng thái ban đầu
    workflow=graph.compile()
    state=workflow.invoke(initial_state)
    print("content State:", state["content_type"])
    print("keywords:", state["keywords"])


if __name__ == "__main__":
    main()
