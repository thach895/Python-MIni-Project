import logging


def show_devices(devices):
    """Hiển thị danh sách thiết bị."""

    if not devices:
        print("Hệ thống hiện không có thiết bị nào.")
        return

    print("\nDANH SÁCH THIẾT BỊ")
    print("-" * 85)
    print(
        f"{'ID':<8}"
        f"{'Location':<25}"
        f"{'Old Index':<15}"
        f"{'New Index':<15}"
        f"{'Status':<15}"
    )
    print("-" * 85)

    for device in devices:
        print(
            f"{device['id']:<8}"
            f"{device['location']:<25}"
            f"{device['old_index']:<15}"
            f"{device['new_index']:<15}"
            f"{device['status']:<15}"
        )


def find_device(devices, device_id):
    """Tìm thiết bị theo ID."""

    for device in devices:
        if device["id"] == device_id:
            return device

    return None


def update_indices(devices):
    """Cập nhật chỉ số điện."""

    device_id = input("Nhập mã thiết bị: ").strip().upper()

    device = find_device(devices, device_id)

    if device is None:
        print("ERR-E01: Không tìm thấy mã thiết bị.")
        logging.error("ERR-E01 - Device not found")
        return

    while True:
        try:
            old_index = int(input("Nhập chỉ số cũ: "))

            if old_index < 0:
                print("Chỉ số phải >= 0.")
                continue

            break

        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

    while True:
        try:
            new_index = int(input("Nhập chỉ số mới: "))

            if new_index < 0:
                print("Chỉ số phải >= 0.")
                continue

            if new_index < old_index:
                print("ERR-E02: Chỉ số mới không được nhỏ hơn chỉ số cũ.")
                continue

            break

        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

    device["old_index"] = old_index
    device["new_index"] = new_index

    logging.info(f"Updated device {device_id}")

    print("Cập nhật dữ liệu thành công.")


def activate_overload(devices):
    """Kích hoạt trạng thái quá tải."""

    device_id = input("Nhập mã thiết bị: ").strip().upper()

    device = find_device(devices, device_id)

    if device is None:
        print("ERR-E01: Không tìm thấy mã thiết bị.")
        logging.error("ERR-E01 - Device not found")
        return

    if device["status"] == "Overload":
        print("ERR-E04: Thiết bị đã ở trạng thái Overload.")
        return

    consumption = (
        device["new_index"] - device["old_index"]
    )

    if consumption > 5000:
        device["status"] = "Overload"

        logging.warning(
            f"Device {device_id} switched to Overload"
        )

        print("Kích hoạt cảnh báo quá tải thành công.")

    else:
        print(
            "Thiết bị chưa vượt ngưỡng 5000 kWh."
        )


def calculate_energy_financials(devices):
    """
    Trả về:
    (
        total_consumption,
        discount_percent,
        final_cost
    )
    """

    total_consumption = 0

    for device in devices:
        total_consumption += (
            device["new_index"]
            - device["old_index"]
        )

    base_cost = total_consumption * 3000

    if total_consumption >= 50000:
        discount_percent = 3
    else:
        discount_percent = 0

    final_cost = (
        base_cost
        - (base_cost * discount_percent / 100)
    )

    return (
        total_consumption,
        discount_percent,
        final_cost
    )


def display_menu():
    print("\n===== SMART ENERGY MONITOR =====")
    print("1. Xem danh sách thiết bị")
    print("2. Cập nhật chỉ số điện")
    print("3. Kích hoạt cảnh báo quá tải")
    print("4. Tính tổng điện năng & chi phí")
    print("5. Thoát")
    print("================================")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    devices = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload"
        }
    ]

    while True:

        display_menu()

        try:
            choice = int(
                input("Chọn chức năng: ")
            )

        except ValueError:
            print("Vui lòng nhập số từ 1 đến 5.")
            continue

        if choice == 1:
            show_devices(devices)

        elif choice == 2:
            update_indices(devices)

        elif choice == 3:
            activate_overload(devices)

        elif choice == 4:

            (
                total_consumption,
                discount_percent,
                final_cost
            ) = calculate_energy_financials(
                devices
            )

            print("\nBÁO CÁO NĂNG LƯỢNG")
            print(
                f"Tổng điện tiêu thụ: "
                f"{total_consumption:,} kWh"
            )
            print(
                f"Chiết khấu áp dụng: "
                f"{discount_percent}%"
            )
            print(
                f"Tổng chi phí sau chiết khấu: "
                f"{final_cost:,.0f} VND"
            )

        elif choice == 5:
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()