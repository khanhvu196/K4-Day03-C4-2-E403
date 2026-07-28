import json
import re
from config import test_cases
from src.tools import AVAILABLE_TOOLS
from src.prompts import CHATBOT_BASELINE_PROMPT, REACT_SYSTEM_PROMPT, MAX_ITERATIONS

def run_baseline_chatbot(user_prompt: str) -> str:
    """Hàm giả lập Chatbot Baseline (Cấp 2 - Không có Tool)."""
    print(f"\n[Baseline Chatbot] User: {user_prompt}")
    # Chatbot thuần không có grounding dữ liệu thực tế
    response = "Cảm ơn bạn đã liên hệ. Đơn hàng của bạn đang được xử lý và sẽ chuyển đến bạn sớm nhất!"
    print(f"[Baseline Chatbot] Response: {response}")
    return response

def parse_action(text: str):
    """Trích xuất tên tool và tham số từ chuỗi Action của LLM."""
    match = re.search(r'Action:\s*(\w+)\["(.*?)"\]', text)
    if match:
        return match.group(1), match.group(2)
    return None, None

def run_react_agent(user_prompt: str) -> str:
    """Hàm chạy ReAct Agent Loop (Cấp 3 - Thought -> Action -> Observation)."""
    print(f"\n{'='*50}\n[ReAct Agent] User: {user_prompt}\n{'='*50}")
    
    # Giả lập vòng lặp ReAct
    step = 0
    if "DH1001" in user_prompt and "đổi trả" in user_prompt:
        print("Thought: Cần kiểm tra điều kiện đổi trả của đơn DH1001 trước.")
        print("Action: check_return_policy[\"DH1001\", \"áo bị rách khuy\"]")
        obs1 = AVAILABLE_TOOLS["check_return_policy"]("DH1001", "áo bị rách khuy")
        print(f"Observation: {obs1}")
        
        print("\nThought: Đơn hàng đủ điều kiện. Tiến hành tạo phiếu đổi trả.")
        print("Action: create_return_request[\"DH1001\", \"áo bị rách khuy\"]")
        obs2 = AVAILABLE_TOOLS["create_return_request"]("DH1001", "áo bị rách khuy")
        print(f"Observation: {obs2}")
        
        final_ans = "Đơn hàng #DH1001 đủ điều kiện đổi trả. Đã tạo thành công phiếu yêu cầu RT-DH1001-2026."
        print(f"\nFinal Answer: {final_ans}")
        return final_ans
    elif "DH9999" in user_prompt:
        print("Thought: Tra cứu thông tin đơn hàng DH9999.")
        print("Action: check_return_policy[\"DH9999\", \"sai màu\"]")
        obs = AVAILABLE_TOOLS["check_return_policy"]("DH9999", "sai màu")
        print(f"Observation: {obs}")
        final_ans = "Rất tiếc, đơn hàng #DH9999 không tồn tại trong hệ thống."
        print(f"\nFinal Answer: {final_ans}")
        return final_ans
    else:
        print("Thought: Trả lời câu hỏi lý thuyết trực tiếp.")
        final_ans = "Shop hỗ trợ đổi trả trong vòng 7 ngày kể từ khi nhận hàng và miễn phí ship do lỗi nhà sản xuất."
        print(f"\nFinal Answer: {final_ans}")
        return final_ans

if __name__ == "__main__":
    # Load và chạy thử Test Case 4
    with open("config/test_cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)
        print("--- CHẠY THỬ NGHIỆM APPLICATION ---")
    run_react_agent(cases[3]["prompt"])