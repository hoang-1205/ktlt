def bingo_1_so(so_tien_hien_co): # Hàm xử lý chức năng 1
    try: # Bắt lỗi khi nhập số mua
        so_mua = int(input("Nhập số muốn mua (0-9): ")) # Nhập số mua
        if so_mua < 0 or so_mua > 9: # Kiểm tra khoảng giá trị
            print("Số mua phải từ 0 đến 9.") # Thông báo lỗi
            return so_tien_hien_co # Trả lại số dư cũ nếu có lỗi để tiếp tục vòng lặp main
    except ValueError: # Bắt lỗi không phải số
        print("Dữ liệu nhập không hợp lệ.") # Thông báo lỗi
        return so_tien_hien_co # Trả lại số dư cũ
        
    tien_cuoc = nhap_tien_cuoc(so_tien_hien_co) # Gọi hàm phụ để lấy tiền cược hợp lệ
    
    bingo_kq = [random.randint(0, 9) for _ in range(3)] # Sinh 3 số ngẫu nhiên
    print(f"Kết quả xổ số: {bingo_kq}") # In kết quả
    
    if so_mua in bingo_kq: # Nếu số mua có trong kết quả
        so_tien_hien_co += tien_cuoc # Cộng tiền lời
        print(f"Chúc mừng! Bạn đã trúng. Số tiền hiện tại: {so_tien_hien_co}") # Thông báo trúng
    else: # Nếu không trúng
        so_tien_hien_co -= tien_cuoc # Trừ tiền cược
        print(f"Rất tiếc! Bạn không trúng. Số tiền còn lại: {so_tien_hien_co}") # Thông báo trượt
        
    return so_tien_hien_co # Trả về số dư sau khi đã cộng/trừ tiền