def tai_xiu_hoa(so_tien_hien_co): # Hàm xử lý chức năng 3
    print("Chọn kết quả:") # Hiển thị tùy chọn
    print("1. Xỉu (Tổng 0-8)") # Chọn xỉu
    print("2. Hòa (Tổng 9-18)") # Chọn hòa
    print("3. Tài (Tổng 19-27)") # Chọn tài
    lua_chon_txh = input("Nhập lựa chọn của bạn (1-3): ") # Nhập từ bàn phím
    if lua_chon_txh not in ['1', '2', '3']: # Nếu nhập sai
        print("Lựa chọn không hợp lệ.") # Báo lỗi
        return so_tien_hien_co # Dừng chức năng
        
    tien_cuoc = nhap_tien_cuoc(so_tien_hien_co) # Nhập tiền cược
    
    bingo_kq = [random.randint(0, 9) for _ in range(3)] # Quay 3 số
    print(f"Kết quả xổ số: {bingo_kq}") # In kết quả
    tong_diem = sum(bingo_kq) # Tính tổng điểm
    print(f"Tổng điểm: {tong_diem}") # In tổng điểm
    
    ket_qua_thuc_te = "" # Tạo chuỗi lưu kết quả
    if 0 <= tong_diem <= 8: # Mốc xỉu
        ket_qua_thuc_te = "1" # Mã cho xỉu
        print("Kết quả là: Xỉu") # In ra xỉu
    elif 9 <= tong_diem <= 18: # Mốc hòa
        ket_qua_thuc_te = "2" # Mã cho hòa
        print("Kết quả là: Hòa") # In ra hòa
    else: # Mốc tài
        ket_qua_thuc_te = "3" # Mã cho tài
        print("Kết quả là: Tài") # In ra tài
        
    if lua_chon_txh == ket_qua_thuc_te: # Nếu chọn đúng
        so_tien_hien_co += tien_cuoc * 0.5 # Ăn 50% tiền cược
        print(f"Chúc mừng! Bạn đã thắng. Số tiền hiện tại: {so_tien_hien_co}") # In thông báo thắng
    else: # Nếu chọn sai
        so_tien_hien_co -= tien_cuoc # Bị trừ tiền cược
        print(f"Rất tiếc! Bạn đoán sai. Số tiền còn lại: {so_tien_hien_co}") # In thông báo thua
        
    return so_tien_hien_co # Trả về số tiền cập nhậti