def main(): # Hàm chính điều khiển luồng chương trình
    try: # Bắt lỗi khi nhập tiền gốc
        so_tien_hien_co = float(input("Nhập số tiền hiện có ban đầu: ")) # Nhập số tiền vào
    except ValueError: # Lỗi không phải là số
        print("Vui lòng nhập một số hợp lệ.") # In cảnh báo
        return # Thoát chương trình

    while True: # Bắt đầu vòng lặp hiển thị menu
        print("\n--- MENU TRÒ CHƠI BINGO ---") # In tiêu đề
        print("1. Bingo 1 số") # Lựa chọn 1
        print("2. Chọn 2 số trùng nhau") # Lựa chọn 2
        print("3. Lớn/ nhỏ/ hòa (Tài/Xỉu/Hòa)") # Lựa chọn 3
        print("4. In số tiền trong tài khoản") # Lựa chọn 4
        print("5. Ghi số tiền còn lại trong tài khoản vào file text và Thoát") # Lựa chọn 5
        
        chon = input("Chọn chức năng (1-5): ") # Yêu cầu người dùng chọn
        
        if chon == '1': # Rẽ nhánh 1
            so_tien_hien_co = bingo_1_so(so_tien_hien_co) # Gọi hàm 1, cập nhật lại biến lưu tiền
        elif chon == '2': # Rẽ nhánh 2
            so_tien_hien_co = bingo_2_so(so_tien_hien_co) # Gọi hàm 2, cập nhật lại biến lưu tiền
        elif chon == '3': # Rẽ nhánh 3
            so_tien_hien_co = tai_xiu_hoa(so_tien_hien_co) # Gọi hàm 3, cập nhật lại biến lưu tiền
        elif chon == '4': # Rẽ nhánh 4
            in_tai_khoan(so_tien_hien_co) # Gọi hàm 4, không cần nhận lại giá trị
        elif chon == '5': # Rẽ nhánh 5
            ghi_file_va_thoat(so_tien_hien_co) # Gọi hàm 5 để lưu file
            break # Phá vỡ vòng lặp (thoát trò chơi)
        else: # Người dùng nhập linh tinh
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.") # Nhắc nhở