# Biến lưu trữ dữ liệu: Mỗi liên hệ là một dict {'name': '...', 'phone': '...'} 
phonebook = [] 
 
def add_contact(): 
    # Nhập tên, sđt -> append vào phonebook 
    print("Đã thêm liên hệ.") 
 
def view_contacts(): 
    # Duyệt list phonebook và in ra 
    # Ví dụ: 1. Nam - 0909xxx 
    pass 
 
def search_contact(): 
    # Nhập tên cần tìm 
    # Duyệt list, so sánh name, in ra phone nếu thấy 
    pass 
 
def main(): 
    while True: 
        print("\n--- DANH BẠ ĐIỆN THOẠI ---") 
        print("1. Thêm liên hệ") 
        print("2. Xem danh bạ") 
        print("3. Tìm kiếm") 
        print("4. Thoát") 
         
        choice = input("Chọn chức năng: ") 
         
        if choice == '1': 
            add_contact() 
        elif choice == '2': 
            view_contacts() 
        elif choice == '3': 
            search_contact() 
        elif choice == '4': 
            print("Tạm biệt!") 
            break 
        else: 
            print("Lựa chọn không hợp lệ.") 
 
if __name__ == "__main__": 
    main()

    def add_contact(name, phone):
    contact = {"name": name, "phone": phone}
    phonebook.append(contact)
    print(f"Đã thêm liên hệ: {name} - {phone}")

elif choice == "1":
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    add_contact(name, phone)
