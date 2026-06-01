saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]
while True :
    print("""===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình""")
    choice = input("Nhập lựa chọn của bạn:")
    match choice :
        case "1" :
            if len(saving_accounts) == 0 :
                print("Danh sách hiện đang trống ")
            else :
                print("Danh sách sổ tiết kiệm :")
                for index,value in enumerate(saving_accounts,start=1):
                    print(f'{index}. | Mã sổ : {value["account_id"]} | Khách hàng: {value["customer_name"]} | Số tiền gửi: {value["balance"]} | Kỳ hạn: {value["term_months"]} tháng | Lãi xuất: {value["interest_rate"]}%/năm| Trạng thái: {value["status"]} ')

        case "2" :
            ma_so = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            found = False
            for account in saving_accounts :
                if account["account_id"] == ma_so:
                    found = True 
                    break
            if found :
                print("Mã sổ tiết kiệm đã tồn tại !")
                continue
            ten_khach_hang = input("Nhập tên khách hàng:").strip()
            if ten_khach_hang == "" :
                print("Tên khách hàng không được để trống")
                continue
            tien_gui = input("Nhập số tiền gửi: ").strip()
            if not tien_gui.isdigit() or int(tien_gui) <= 0 :
                print("Tiền gửi phải là số nguyên dương")
                continue
            ky_han = input("Nhập kỳ hạn gửi theo tháng: ")
            if not ky_han.isdigit() or int(ky_han) <= 0 :
                print("Kỳ hạn gửi phải là số nguyên dương")
                continue
            lai_suat = float(input("Nhập lãi xuất năm: ").strip())
            if lai_suat <= 0:
                print("Lãi suất phải là số thực lớn hơn 0")
                continue
            saving_accounts.append({
                "account_id": ma_so,
                "customer_name": ten_khach_hang,
                "balance": tien_gui,
                "term_months": ky_han,
                "interest_rate": lai_suat,
                "status": "active"
                })
            print("Mở sổ tiết kiệm thành công")
        case "3" :
            ma_update = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            found = False
            for i in saving_accounts :
                if i["account_id"] == ma_update :
                    found = True
                    if i["status"] == "closed":
                        print( "Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break
                    new_name = input("Nhập tên khahcs hàng mới: ").strip()
                    if new_name == "" :
                        print("Tên mới không được để trống")
                        break
                    price_new = input("Nhập số tiền gửi mới").strip()
                    if not price_new.isdigit() or int(price_new) <= 0 :
                        print("Tiền gửi phải là số nguyên dương")
                        break
                    term_new = input("Nhập kỳ hạn gửi theo tháng mới: ")
                    if not term_new.isdigit() or int(term_new) <= 0 :
                        print("Kỳ hạn gửi phải là số nguyên dương")
                        break
                    interest_rate_new = float(input("Nhập lãi xuất năm: ").strip())
                    if interest_rate_new <= 0:
                        print("Lãi suất phải là số thực lớn hơn 0")
                        break
                    i["customer_name"] = new_name
                    i["balance"] = price_new
                    i["term_months"] = term_new
                    i["interest_rate"] = interest_rate_new

                    print("Cập nhật thành công!")
                    break
            if not found :
                print("Không tìm thấy mã sổ tiết kiệm ! ")
                continue
        case "4" :
            account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            found = False
            for i in saving_accounts :
                if i["account_id"] == account_id :
                    i["status"] = "closed"
                    found = True 
                    print("Tất toán thành công !")
                    break
            if not found :
                print("Không tìm thấy mã sổ tiết kiệm !")
        case "5" :
            account_id = input("Nhập mã sổ tiết kiệm cần tính lãi : ").strip().upper()
            found = False
            for i in saving_accounts :
                if i["account_id"] == account_id :
                    found = True
                    if i["status"] == "closed":
                        print( "Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break
                    interest =( i["balance"] * i["interest_rate"] / 100 * i["term_months"] /12)
                    total_amountn = i["balance"] + interest

                    print("Tiền lãi dự kiến : ", interest)
                    print("Tổng tiền khi đến hạn: ",total_amountn)
                    break
            if not found :
                print("Không tìm thấy mã sổ tiết kiệm !")
        case "6":
            account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            found = False
            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = True
                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                    sending_month = input("Nhập số tháng thực gửi: ").strip()
                    if not sending_month.isdigit() or int(sending_month) <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                    sending_month = int(sending_month)
                    if sending_month < account["term_months"]:
                        lai_suat = 0.5
                        print("Khách hàng rút trước hạn")
                    else:
                        lai_suat = account["interest_rate"]
                        print("Khách hàng đủ điều kiện hưởng lãi đúng hạn")
                    interest = (account["balance"]* lai_suat / 100 * sending_month / 12)
                    total_amountn = account["balance"] + interest
                    print("Tiền lãi thực nhận:", interest)
                    print("Tổng tiền thực nhận:", total_amountn)
                    break
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")
        case "7" :
            print("Thoát chương trình")
            break
        case _ :
            print("\nNhập lựa chọn không phải số từ 1-7 hoặc nhập chữ.Vui lòng nhập lại !")
            continue

