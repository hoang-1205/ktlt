def ghi_file_va_thoat(so_tien_hien_co): # Hàm xử lý chức năng 5
    try: # Bắt lỗi khi thao tác với file
        with open("account_balance.txt", "w", encoding="utf-8") as f: # Mở (hoặc tạo) file để ghi đè
            f.write(f"Số tiền còn lại trong tài khoản: {so_tien_hien_co}") # Tiến hành ghi thông tin
        print("Đã ghi số tiền còn lại vào file 'account_balance.txt'.") # Báo thành công
    except Exception as e: # Bắt các lỗi file không lường trước
        print(f"Có lỗi khi ghi file: {e}") # In thông báo lỗi
    print("Cảm ơn bạn đã chơi! Hẹn gặp lại.") # Lời chào tạm biệt