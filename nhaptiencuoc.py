def nhap_tien_cuoc(so_tien_hien_co): # Hàm phụ để tái sử dụng việc nhập tiền cược
    while True: # Vòng lặp yêu cầu nhập lại nếu sai
        try: # Bắt lỗi nhập liệu
            tien_cuoc = float(input("Nhập số tiền đặt cược: ")) # Nhập tiền cược
            if 0 < tien_cuoc <= so_tien_hien_co: # Kiểm tra tiền cược hợp lệ (lớn hơn 0 và không vượt quá số dư)
                return tien_cuoc # Trả về số tiền cược nếu hợp lệ
            print("Số tiền cược không hợp lệ hoặc lớn hơn số tiền hiện có.") # Thông báo lỗi
        except ValueError: # Bắt lỗi nếu nhập không phải là số
            print("Dữ liệu nhập không hợp lệ.") # Thông báo lỗi