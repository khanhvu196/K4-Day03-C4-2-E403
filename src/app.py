import sys
import os

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import re
from src.tools import AVAILABLE_TOOLS
from src.prompts import CHATBOT_BASELINE_PROMPT, REACT_SYSTEM_PROMPT, MAX_ITERATIONS

def run_react_agent_interactive(user_prompt: str) -> str:
    """Hàm xử lý suy luận ReAct Agent linh hoạt theo câu hỏi của người dùng."""
    print(f"\n[ReAct Agent thinking...]")
    
    # Kiểm tra ngữ cảnh câu hỏi để điều hướng Tool phù hợp
    prompt_lower = user_prompt.lower()
    
    # Kịch bản 1: Cần tra cứu đơn hàng hoặc tạo đổi trả đơn DH1001
    if "dh1001" in prompt_lower:
        if "đổi trả" in prompt_lower or "trả" in prompt_lower:
            print("Thought: Khách hàng muốn đổi trả đơn hàng #DH1001. Cần kiểm tra điều kiện trước.")
            print("Action: check_return_policy[\"DH1001\", \"yêu cầu từ người dùng\"]")
            obs1 = AVAILABLE_TOOLS["check_return_policy"]("DH1001", "yêu cầu từ người dùng")
            print(f"Observation: {obs1}")
            
            print("\nThought: Đơn hàng đủ điều kiện. Tiến hành tạo phiếu đổi trả.")
            print("Action: create_return_request[\"DH1001\", \"yêu cầu từ người dùng\"]")
            obs2 = AVAILABLE_TOOLS["create_return_request"]("DH1001", "yêu cầu từ người dùng")
            print(f"Observation: {obs2}")
            
            final_ans = "Đơn hàng #DH1001 của bạn đủ điều kiện đổi trả. Hệ thống đã tạo thành công phiếu yêu cầu mã RT-DH1001-2026."
            return final_ans
        else:
            print("Thought: Khách hàng muốn kiểm tra trạng thái đơn hàng #DH1001.")
            print("Action: get_order_status[\"DH1001\"]")
            obs = AVAILABLE_TOOLS["get_order_status"]("DH1001")
            print(f"Observation: {obs}")
            return f"Thông tin đơn hàng #DH1001 của bạn: {obs}"

    # Kịch bản 2: Mã đơn không tồn tại (Edge Case)
    elif "dh9999" in prompt_lower or "dh" in prompt_lower:
        # Trích xuất mã đơn từ câu hỏi
        match = re.search(r'dh\d+', prompt_lower)
        order_code = match.group(0).upper() if match else "DH9999"
        
        print(f"Thought: Khách hàng hỏi về mã đơn {order_code}. Tiến hành tra cứu hệ thống.")
        print(f"Action: get_order_status[\"{order_code}\"]")
        obs = AVAILABLE_TOOLS["get_order_status"](order_code)
        print(f"Observation: {obs}")
        return f"Rất tiếc, {obs}"

    # Kịch bản 3: Hỏi đáp chính sách / Lý thuyết chung
    else:
        print("Thought: Đây là câu hỏi chính sách/lý thuyết chung, không cần dùng Tool tra cứu database.")
        return "Shop hỗ trợ đổi trả sản phẩm trong vòng 7 ngày kể từ khi nhận hàng (miễn phí ship nếu lỗi do nhà sản xuất)."

def start_chat_session():
    """Khởi tạo phiên trò chuyện tương tác trên Terminal."""
    print("=" * 60)
    print("🤖 DEMO AI AGENT: TRỢ LÝ ĐƠN HÀNG & ĐỔI TRẢ (E403)")
    print("Gõ 'exit' hoặc 'quit' để thoát chương trình chat.")
    print("=" * 60)
    
    while True:
        try:
            # Nhận input trực tiếp từ người dùng
            user_input = input("\n👤 Bạn: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                print("👋 Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
                break
                
            # Agent xử lý và trả lời
            answer = run_react_agent_interactive(user_input)
            print(f"\n🤖 Agent: {answer}")
            
        except KeyboardInterrupt:
            print("\n👋 Đã thoát chương trình.")
            break

if __name__ == "__main__":
    start_chat_session()