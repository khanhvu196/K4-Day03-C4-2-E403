import json

# Dữ liệu giả lập (Mock Database)
MOCK_ORDERS = {
    "DH1001": {"status": "Đã giao thành công", "date": "2026-07-25", "items": "Áo sơ mi nam", "price": 350000},
    "DH1002": {"status": "Đang vận chuyển", "date": "2026-07-27", "items": "Quần Jeans", "price": 500000}
}

def get_order_status(order_id: str) -> str:
    """Tra cứu thông tin và trạng thái chi tiết của một đơn hàng theo mã order_id."""
    order = MOCK_ORDERS.get(order_id.upper())
    if order:
        return json.dumps(order, ensure_ascii=False)
    return f"LỖI: Không tìm thấy đơn hàng mã '{order_id}' trong hệ thống."

def check_return_policy(order_id: str, reason: str) -> str:
    """Kiểm tra xem đơn hàng có đủ điều kiện đổi trả hay không dựa trên mã đơn và lý do."""
    order = MOCK_ORDERS.get(order_id.upper())
    if not order:
        return f"LỖI: Mã đơn '{order_id}' không tồn tại."
    if order["status"] != "Đã giao thành công":
        return f"LỖI: Đơn hàng '{order_id}' chưa giao thành công, không thể tạo yêu cầu đổi trả."
    return f"THÀNH CÔNG: Đơn hàng '{order_id}' đủ điều kiện đổi trả với lý do '{reason}'."

def create_return_request(order_id: str, reason: str) -> str:
    """Tạo phiếu yêu cầu đổi trả chính thức cho đơn hàng."""
    return f"XÁC NHẬN: Đã tạo thành công phiếu đổi trả cho đơn '{order_id}'. Mã phiếu: RT-{order_id}-2026."

# Đăng ký các công cụ vào Registry
AVAILABLE_TOOLS = {
    "get_order_status": get_order_status,
    "check_return_policy": check_return_policy,
    "create_return_request": create_return_request
}