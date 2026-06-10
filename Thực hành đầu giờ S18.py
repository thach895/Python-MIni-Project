products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if not products_list:
        print("Cửa hàng của bạn chưa có sản phẩm nào")
        return
    print("__Danh Sách Sản Phẩm__")
    print("{:<5}|{:<20}|{:>10}".format("ID", "Tên Sản phẩm", "Giá Bán"))
    for item in products_list:
        print("{:<5}|{:<20}|{:>10}".format(
            item["id"],
            item["name"],
            item["price"]
        ))
def add_product(products_list):
    new_id=input("Nhập Id:")
    new_name=input("Nhập tên:");
    new_price=input()

while True:
    print("=======Quản Lý Cửa Hàng - Mini Store========");
    print("1.Xem danh sách sản phẩm hiện có");
    print("2.Thêm mới 1 sản phẩm");
    print("3.Cập nhật giá sản phẩm theo ID");
    print("4.Thoát chương trình");
    choice=input("Nhập lựa chọn:");

    match choice:
        case "1":
            show_products(products)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case _:
            print("Lựa chọn không phù hợp!")