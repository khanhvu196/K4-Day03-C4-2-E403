# 📊 BÁO CÁO ĐÁNH GIÁ & TRACE LOGS - LAB 3
**Chủ đề chọn:** Đề tài 5 - Trợ Lý Tra Cứu Đơn Hàng & Xử Lý Đổi Trả

---

## 1. AGENTIC FIT EVALUATION (SCORING MATRIX)

| Tiêu chí đánh giá | Điểm (1-5) | Lý giải chi tiết cho Đề tài 5 |
| :--- | :---: | :--- |
| **1. Tính thời gian thực & dữ liệu động** | 5/5 | Trạng thái đơn hàng (#DH1001) và kho bãi thay đổi liên tục, không thể dùng kiến thức tĩnh của LLM. |
| **2. Độ phức tạp đa bước (Multi-step Reasoning)** | 5/5 | Cần kiểm tra đơn hàng -> tra cứu điều kiện chính sách -> khởi tạo phiếu đổi trả chính thức. |
| **3. Tác động hành động (Side Effects)** | 4/5 | Việc khởi tạo yêu cầu đổi trả làm thay đổi trạng thái trong database hệ thống. |
| **4. Biên rủi ro & Xử lý lỗi (Edge Cases)** | 4/5 | Cần xử lý các trường hợp nhập sai mã đơn, đơn chưa giao hoặc quá hạn 7 ngày đổi trả. |

> **Tổng điểm Agentic Fit:** **18/20** ➔ **Rất thích hợp để xây dựng ReAct Agent.**

---

## 2. NHẬT KÝ KIỂM THỬ (TRACE LOGS)
*(Sẽ cập nhật ở Mốc 2 và Mốc 3)*