parking_lot = []
next_id = 1

while True:
    print("\n========== SMART PARKING SYSTEM ==========")
    print("1. Check-in xe")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out xe")
    print("5. Thoát")
    print("==========================================")

    try:
        choice = int(input("Chọn chức năng (1-5): "))
    except ValueError:
        print("ERR-01: Vui lòng nhập số từ 1 đến 5")
        continue

    if choice == 1:

        while True:
            plate = input("Nhập biển số: ").strip().upper()

            if plate == "":
                print("ERR-01: Biển số không được để trống")
                continue

            duplicate = False

            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    duplicate = True
                    break

            if duplicate:
                print("ERR-02: Biển số đã tồn tại trong hệ thống")
            else:
                break

        while True:
            try:
                vehicle_type = int(
                    input("Loại xe (1-Xe máy, 2-Ô tô): ")
                )

                if vehicle_type == 1:
                    vehicle_type = "Xe máy"
                    break

                elif vehicle_type == 2:
                    vehicle_type = "Ô tô"
                    break

                else:
                    print("Chỉ được nhập 1 hoặc 2")

            except ValueError:
                print("Vui lòng nhập số")

        while True:
            try:
                entry_time = int(input("Nhập giờ vào (0-24): "))
                break
            except ValueError:
                print("Vui lòng nhập số nguyên")

        vehicle = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }

        parking_lot.append(vehicle)
        next_id += 1

        print("Check-in thành công!")

    elif choice == 2:

        if len(parking_lot) == 0:
            print("ERR-03: Bãi xe hiện đang trống")
        else:
            print("\n{:<5} {:<15} {:<10} {:<10}".format(
                "ID", "Biển số", "Loại xe", "Giờ vào"
            ))

            print("-" * 45)

            for vehicle in parking_lot:
                print("{:<5} {:<15} {:<10} {:<10}".format(
                    vehicle["id"],
                    vehicle["plate"],
                    vehicle["type"],
                    vehicle["entry_time"]
                ))

    elif choice == 3:

        plate = input("Nhập biển số cần tìm: ").strip().upper()

        if plate == "":
            print("ERR-01: Biển số không được để trống")
            continue

        found = None

        for vehicle in parking_lot:
            if vehicle["plate"] == plate:
                found = vehicle
                break

        if found:
            print(found)
        else:
            print("ERR-04: Không tìm thấy biển số trong hệ thống")

    elif choice == 4:

        plate = input("Nhập biển số cần check-out: ").strip().upper()

        if plate == "":
            print("ERR-01: Biển số không được để trống")
            continue

        vehicle_found = None

        for vehicle in parking_lot:
            if vehicle["plate"] == plate:
                vehicle_found = vehicle
                break

        if vehicle_found is None:
            print("ERR-04: Không tìm thấy biển số trong hệ thống")

        else:

            while True:
                try:
                    check_out_time = int(
                        input("Nhập giờ ra (0-24): ")
                    )

                    if check_out_time < vehicle_found["entry_time"]:
                        print(
                            "ERR-05: Giờ ra không hợp lệ (phải >= giờ vào)"
                        )
                    else:
                        break

                except ValueError:
                    print("Vui lòng nhập số nguyên")

            parking_time = (
                check_out_time - vehicle_found["entry_time"]
            )

            if vehicle_found["type"] == "Xe máy":
                fee = parking_time * 5000
            else:
                fee = parking_time * 20000

            print("\n===== THÔNG TIN THANH TOÁN =====")
            print(f"Biển số : {vehicle_found['plate']}")
            print(f"Loại xe : {vehicle_found['type']}")
            print(f"Giờ vào : {vehicle_found['entry_time']}")
            print(f"Giờ ra  : {check_out_time}")
            print(f"Số giờ gửi: {parking_time}")
            print(f"Phí gửi xe: {fee:,} VNĐ")

            parking_lot.remove(vehicle_found)

            print("Check-out thành công!")

    elif choice == 5:
        print("Đã thoát chương trình!")
        break

    else:
        print("ERR-01: Chọn từ 1 đến 5")