from config import MENU


def print_menu():
    print("\n=========================================")
    print("           WELCOME TO BITE & GO          ")
    print("=========================================")
    print(f"{'Code':<6} | {'Item Name':<23} | {'Price':<8}")
    print("-----------------------------------------")
    for code, item in MENU.items():
        print(f"[{code}]    | {item['name']:<23} | ₱{item['price']:<7.2f}")
    print("=========================================\n")


def print_receipt(orders, subtotal, discount, final_total):
    print("\n" + "=" * 43)
    print("               BITE & GO                 ")
    print("          123 MAIN STREET, CEBU          ")
    print("          OFFICIAL RECEIPT               ")
    print("=" * 43)
    print(f"{'Qty':<4} {'Item Description':<20} {'Price':<8} {'Total':<8}")
    print("-" * 43)

    for item in orders:
        print(f"{item['quantity']:<4} {item['name']:<20} ₱{item['price']:<7.2f} ₱{item['line_total']:<7.2f}")

    print("-" * 43)
    print(f"{'Subtotal:':<32} ₱{subtotal:>8.2f}")
    if discount > 0:
        print(f"{'Discount (10%):':<32}-₱{discount:>8.2f}")
    print(f"{'TOTAL AMOUNT DUE:':<32} ₱{final_total:>8.2f}")
    print("=" * 43)
    print("       THANK YOU FOR DINING WITH US!     ")
    print("=" * 43 + "\n")


def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        print("[x] Invalid input. Please answer with 'yes' or 'no'.")


def get_valid_item_code():
    while True:
        try:
            code = int(input("Enter Item Code: "))
            if code in MENU:
                return code
            print("[x] Item code not found. Please choose from the menu.")
        except ValueError:
            print("[x] Invalid input. Please enter a valid numerical Item Code.")


def get_valid_quantity():
    while True:
        try:
            qty = int(input("Enter Quantity: "))
            if qty > 0:
                return qty
            print("[x] Quantity must be at least 1.")
        except ValueError:
            print("[x] Invalid input. Please enter a positive integer.")