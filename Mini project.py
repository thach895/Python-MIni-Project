from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    def __init__(self, brand: str):
        self.brand = brand
        self.__odometer = 0

    @property
    def odometer(self):
        return self.__odometer

    def drive(self, distance: float):
        if distance > 0:
            self.__odometer += distance
            print(f"[{self.brand}] Đã di chuyển thêm {distance} km.")
        else:
            print("[Lỗi] Quãng đường di chuyển phải lớn hơn 0!")

    @abstractmethod
    def calculate_efficiency(self):
        pass

    def __lt__(self, other):
        if not isinstance(other, BaseVehicle):
            return NotImplemented
        return self.__odometer < other.__odometer

class ElectricBus(BaseVehicle):
    def __init__(self, brand: str, battery_capacity: float):
        super().__init__(brand)
        self.battery_capacity = battery_capacity  # kWh

    def calculate_efficiency(self):
        return 1.2

    @staticmethod
    def validate_battery(capacity: float) -> bool:
        return isinstance(capacity, (int, float)) and capacity > 0

class AutonomousFeature:
    def __init__(self, software_version: str):
        self.software_version = software_version

    def navigate(self):
        return f"Hệ thống tự hành phiên bản {self.software_version} đang quét bản đồ và điều khiển phương tiện."

class RoboBus(ElectricBus, AutonomousFeature):
    def __init__(self, brand: str, battery_capacity: float, software_version: str):
        ElectricBus.__init__(self, brand, battery_capacity)
        AutonomousFeature.__init__(self, software_version)

    def calculate_efficiency(self):
        return 1.5

    def show_info(self):
        print(f"--- Thông tin RoboBus ---")
        print(f"Thương hiệu: {self.brand}")
        print(f"Dung lượng pin: {self.battery_capacity} kWh")
        print(f"Số km đã đi: {self.odometer} km")
        print(f"Trạng thái: {self.navigate()}")

if __name__ == "__main__":
    print("=== Đang kiểm tra Thẩm định Dữ liệu (Staticmethod) ===")
    pin_hop_le = ElectricBus.validate_battery(100)
    pin_khong_hop_le = ElectricBus.validate_battery(-50)
    print(f"Kiểm tra pin 100 kWh: {'Hợp lệ' if pin_hop_le else 'Không hợp lệ'}")
    print(f"Kiểm tra pin -50 kWh: {'Hợp lệ' if pin_khong_hop_le else 'Không hợp lệ'}\n")

    print("=== Khởi tạo các phương tiện ===")
    bus_truyen_thong = ElectricBus("VinBus E-Standard", 150)
    robo_bus_vip = RoboBus("VinBus Robo-X", 200, "v4.2.1")
    
    robo_bus_vip.show_info()
    print()

    print("=== Vận hành phương tiện (Cập nhật Odometer) ===")
    bus_truyen_thong.drive(45.5)
    bus_truyen_thong.drive(20.0)
    robo_bus_vip.drive(50.0)
    print()

    print("=== Phân tích Thứ tự tìm kiếm phương thức (MRO) ===")
    print("Thứ tự tìm kiếm phương thức của lớp RoboBus:")
    for i, cls in enumerate(RoboBus.__mro__, start=1):
        print(f"  {i}. {cls.__name__}")
    print()

    print("=== Nạp chồng toán tử so sánh (__lt__) ===")
    print(f"Quãng đường VinBus E-Standard: {bus_truyen_thong.odometer} km")
    print(f"Quãng đường VinBus Robo-X: {robo_bus_vip.odometer} km")
    
    if bus_truyen_thong < robo_bus_vip:
        print("-> Kết quả xếp hạng: VinBus E-Standard đi ít km hơn VinBus Robo-X.")
    else:
        print("-> Kết quả xếp hạng: VinBus Robo-X đi ít km hơn hoặc bằng VinBus E-Standard.")