from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# print("Gemini API Key loaded:", GEMINI_API_KEY is not None)
# print("GEMINI_API_KEY:", GEMINI_API_KEY)
class LLM :
    def __init__(self, api_key : str, model_name : str, max_tokens : int, temperature : float = 1.0) :
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.llm= ChatGoogleGenerativeAI(model=model_name, google_api_key=self.api_key, temperature=self.temperature, max_output_tokens=self.max_tokens)


if __name__ == "__main__":
    print("Testing LLM class...")
    llm = LLM(api_key=GEMINI_API_KEY, model_name="gemini-2.0-flash", max_tokens=1024, temperature=1.0)
    print("LLM instance created with model:", llm.model_name)
    question = "Bạn là ai?"
    answer = llm.llm.invoke(question)
    print("LLM invocation result:", answer.content)
    """
    Ví dụ ở trên, basic_agent đã phản hồi được câu hỏi đặt ra.
    Tuy nhiên cần huấn luyện để Agent hiểu nó là trợ lý ảo Linh Linh.
    Để làm được điều đó, chúng ta bổ sung thêm thông tin vào role "system" khi truyền thông tin lên.
    """
    """
    Cách dịch vụ LLM có quy ước 3 role mô tả nội dung phiên chat:

    - system    - Hệ thống	  - Thiết lập bối cảnh, hướng dẫn mô hình cách phản hồi (giống như "đặt vai trò")
    - user	    - Người dùng  - Nội dung, câu hỏi mà người dùng nhập vào
    - assistant - Trợ lý AI	  - Phản hồi của mô hình (AI) với người dùng
    """
    question = [{
                    "role": "system",
                    "content": "Bạn là Linh Linh, trợ lý ảo. Hãy luôn trả lời tiếng Việt",
                },
                {
                    "role": "user",
                    "content": "2 nhân 3 bằng bao nhiêu?",
                }]
    answer = llm.llm.invoke(question)

    # In kết quả
    print("Human: " + question[-1]["content"])
    print("AI: " + answer.content)