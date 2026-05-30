import random # Thư viện random dùng để sinh số ngẫu nhiên

def nhap_tien_cuoc(so_tien_hien_co): # Hàm phụ để tái sử dụng việc nhập tiền cược
    while True: # Vòng lặp yêu cầu nhập lại nếu sai
        try: # Bắt lỗi nhập liệu
            tien_cuoc = float(input("Nhập số tiền đặt cược: ")) # Nhập tiền cược
            if 0 < tien_cuoc <= so_tien_hien_co: # Kiểm tra tiền cược hợp lệ (lớn hơn 0 và không vượt quá số dư)
                return tien_cuoc # Trả về số tiền cược nếu hợp lệ
            print("Số tiền cược không hợp lệ hoặc lớn hơn số tiền hiện có.") # Thông báo lỗi
        except ValueError: # Bắt lỗi nếu nhập không phải là số
            print("Dữ liệu nhập không hợp lệ.") # Thông báo lỗi

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
        
    return so_tien_hien_co # Trả về số tiền cập nhật

def in_tai_khoan(so_tien_hien_co): # Hàm xử lý chức năng 4
    print(f"Số tiền hiện tại trong tài khoản của bạn là: {so_tien_hien_co}") # In số tiền hiện tại

def ghi_file_va_thoat(so_tien_hien_co): # Hàm xử lý chức năng 5
    try: # Bắt lỗi khi thao tác với file
        with open("account_balance.txt", "w", encoding="utf-8") as f: # Mở (hoặc tạo) file để ghi đè
            f.write(f"Số tiền còn lại trong tài khoản: {so_tien_hien_co}") # Tiến hành ghi thông tin
        print("Đã ghi số tiền còn lại vào file 'account_balance.txt'.") # Báo thành công
    except Exception as e: # Bắt các lỗi file không lường trước
        print(f"Có lỗi khi ghi file: {e}") # In thông báo lỗi
    print("Cảm ơn bạn đã chơi! Hẹn gặp lại.") # Lời chào tạm biệt

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

if __name__ == "__main__": # Kiểm tra xem script có đang chạy như luồng chính không
    main() # Kích hoạt hàm main()
