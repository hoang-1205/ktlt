def bingo_2_so(so_tien_hien_co): # Hàm xử lý chức năng 2
    try: # Bắt lỗi nhập số
        so_mua = int(input("Nhập số muốn mua (0-9): ")) # Nhập số mua
        if so_mua < 0 or so_mua > 9: # Kiểm tra điều kiện
            print("Số mua phải từ 0 đến 9.") # Báo lỗi
            return so_tien_hien_co # Dừng chức năng và trả lại tiền
    except ValueError: # Bắt lỗi nhập chữ
        print("Dữ liệu nhập không hợp lệ.") # Báo lỗi
        return so_tien_hien_co # Dừng chức năng
        
    tien_cuoc = nhap_tien_cuoc(so_tien_hien_co) # Lấy số tiền cược
    
    bingo_kq = [random.randint(0, 9) for _ in range(3)] # Quay xổ số
    print(f"Kết quả xổ số: {bingo_kq}") # In kết quả
    
    if bingo_kq.count(so_mua) >= 2: # Nếu số mua xuất hiện từ 2 lần trở lên
        so_tien_hien_co += tien_cuoc * 2 # Cộng 2 lần tiền cược
        print(f"Chúc mừng! Bạn đã trúng. Số tiền hiện tại: {so_tien_hien_co}") # Báo trúng
    else: # Nếu xuất hiện ít hơn 2 lần
        so_tien_hien_co -= tien_cuoc # Bị trừ tiền cược
        print(f"Rất tiếc! Bạn không trúng. Số tiền còn lại: {so_tien_hien_co}") # Báo thua
        
    return so_tien_hien_co # Trả về số dư mới