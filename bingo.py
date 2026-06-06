import random  # nhập module random để sinh số ngẫu nhiên

SAVE_FILE = "so_tien_con_lai.txt"  # tên file để lưu số tiền còn lại


def nhap_tien_ban_dau(prompt):  # hàm nhập số tiền ban đầu
    while True:
        try:
            value = float(input(prompt).strip())  # đọc chuỗi, bỏ khoảng trắng, chuyển thành float
            if value > 0:
                return value  # trả về khi giá trị hợp lệ
            print("Vui lòng nhập số lớn hơn 0.")  # yêu cầu nhập lại nếu không dương
        except ValueError:
            print("Dữ liệu không hợp lệ. Hãy nhập một số.")  # thông báo nếu nhập sai định dạng


def nhap_so_nguyen(prompt, min_value, max_value):  # hàm nhập số nguyên trong khoảng cố định
    while True:
        try:
            value = int(input(prompt).strip())  # đọc và chuyển sang số nguyên
            if min_value <= value <= max_value:
                return value  # trả về nếu hợp lệ
            print(f"Vui lòng nhập số nguyên từ {min_value} đến {max_value}.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Hãy nhập một số nguyên.")


def ghi_so_tien(balance):  # hàm ghi số tiền còn lại vào file
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:  # mở file ở chế độ ghi
            f.write(f"Số tiền còn lại: {balance:.2f}\n")  # ghi số tiền với 2 chữ số thập phân
    except OSError as exc:
        print(f"Không thể ghi file: {exc}")  # hiển thị lỗi nếu ghi file không được


def quay_so():  # hàm tạo 3 số ngẫu nhiên từ 0 đến 9
    return [random.randint(0, 9) for _ in range(3)]


def dinh_dang_quay(quay):  # hàm chuyển danh sách số thành chuỗi hiển thị
    return " ".join(str(x) for x in quay)


def nhap_tien_cuoc(balance):  # hàm nhập tiền cược và kiểm tra số dư đủ
    while True:
        amount = nhap_tien_ban_dau("Nhập số tiền cược: ")  # yêu cầu người chơi nhập tiền cược
        if amount <= balance:
            return amount  # nếu còn đủ tiền thì trả về
        print("Số tiền cược không được lớn hơn số tiền hiện có.")


def bingo_1_so(balance):  # chức năng Bingo 1 số
    print("\n--- Bingo 1 số ---")
    choice = nhap_so_nguyen("Chọn 1 số từ 0 đến 9: ", 0, 9)  # người chơi chọn 1 số
    amount = nhap_tien_cuoc(balance)  # nhập tiền cược
    draw = quay_so()  # quay 3 số ngẫu nhiên
    print(f"Kết quả xổ số: {dinh_dang_quay(draw)}")  # in kết quả
    if choice in draw:
        reward = amount  # thắng nhân đôi số tiền cược (lợi nhuận = 1 lần cược)
        balance += reward
        print(f"Bạn đã thắng! Số {choice} xuất hiện. Nhận được thêm {reward:.2f}.")
    else:
        balance -= amount  # thua mất tiền cược
        print(f"Bạn đã thua. Số {choice} không xuất hiện. Mất {amount:.2f}.")
    return balance  # trả về số dư cập nhật


def bingo_2_so(balance):  # chức năng chọn 2 số trùng nhau
    print("\n--- Chọn 2 số trùng nhau ---")
    choice = nhap_so_nguyen("Chọn 1 số từ 0 đến 9: ", 0, 9)  # chọn số dự đoán
    amount = nhap_tien_cuoc(balance)  # nhập tiền cược
    draw = quay_so()  # quay 3 số
    print(f"Kết quả xổ số: {dinh_dang_quay(draw)}")
    same_count = draw.count(choice)  # đếm số lần xuất hiện của số chọn
    if same_count >= 2:
        reward = amount * 2  # thắng nhân ba tổng số tiền cược (lợi nhuận = 2 lần cược)
        balance += reward
        print(f"Chúc mừng! Số {choice} xuất hiện {same_count} lần. Nhận được thêm {reward:.2f}.")
    else:
        balance -= amount  # nếu không đúng 2 số thì thua
        print(f"Bạn thua. Số {choice} xuất hiện {same_count} lần. Mất {amount:.2f}.")
    return balance  # trả về số dư sau cược


def tai_xiu_hoa(balance):  # chức năng cược Tài / Xỉu / Hòa
    print("\n--- Tài / Xỉu / Hòa ---")
    print("1. Xỉu (tổng 0-8)")
    print("2. Hòa (tổng 9-18)")
    print("3. Tài (tổng 19-27)")
    choice = nhap_so_nguyen("Chọn loại cược (1-3): ", 1, 3)  # chọn loại cược
    amount = nhap_tien_cuoc(balance)  # nhập tiền cược
    draw = quay_so()  # quay 3 số
    total = sum(draw)  # tính tổng 3 số
    print(f"Kết quả xổ số: {dinh_dang_quay(draw)} (tổng = {total})")
    if total <= 8:
        result = 1  # Xỉu
    elif total <= 18:
        result = 2  # Hòa
    else:
        result = 3  # Tài

    if choice == result:
        reward = amount * 0.5  # thắng được 50% số tiền cược
        balance += reward
        print(f"Bạn thắng! Nhận được thêm {reward:.2f}.")
    else:
        balance -= amount  # thua mất tiền cược
        print(f"Bạn thua. Mất {amount:.2f}.")
    return balance  # trả về số dư cập nhật


def main():  # hàm chính điều khiển menu
    print("=== TRÒ CHƠI BINGO ===")
    balance = nhap_tien_ban_dau("Nhập số tiền hiện có ban đầu: ")  # nhập số dư ban đầu
    while True:
        print("\n--- MENU ---")
        print("1. Bingo 1 số")
        print("2. Chọn 2 số trùng nhau")
        print("3. Lớn / nhỏ / hòa")
        print("4. In số tiền trong tài khoản")
        print("5. Ghi số tiền còn lại vào file và thoát")
        choice = nhap_so_nguyen("Chọn chức năng (1-5): ", 1, 5)  # chọn chức năng

        if choice == 1:
            balance = bingo_1_so(balance)  # xử lý bingo 1 số
        elif choice == 2:
            balance = bingo_2_so(balance)  # xử lý chọn 2 số trùng nhau
        elif choice == 3:
            balance = tai_xiu_hoa(balance)  # xử lý lớn/nhỏ/hòa
        elif choice == 4:
            print(f"Số tiền hiện có: {balance:.2f}")  # in số dư tài khoản
        elif choice == 5:
            ghi_so_tien(balance)  # lưu số dư vào file
            print(f"Đã lưu số tiền còn lại vào '{SAVE_FILE}'.")
            print("Cảm ơn bạn đã chơi!")
            break  # thoát chương trình

        if balance <= 0:
            print("Bạn đã hết tiền. Trò chơi kết thúc.")
            ghi_so_tien(balance)  # lưu số dư khi hết tiền
            print(f"Số dư đã được lưu vào '{SAVE_FILE}'.")
            break  # dừng vòng lặp khi hết tiền


if __name__ == "__main__":
    main()  # chạy chương trình chính
