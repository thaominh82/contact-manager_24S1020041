def view_contacts():
    if not phonebook:
        print("Danh bạ trống.")
        return
    
    print("\n--- DANH BẠ ---")
    for i, contact in enumerate(phonebook, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
