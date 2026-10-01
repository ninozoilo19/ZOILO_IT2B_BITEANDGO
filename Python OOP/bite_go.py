class POSSystem:
    def __init__(self, menu: dict):
        self.menu = menu
        self.orders = []

    def display_menu(self):
        print("\n=========================================")
        print("           WELCOME TO BITE & GO          ")
        print("=========================================")
        print(f"{'Code':<6} | {'Item Name':<23} | {'Price':<8}")
        print("-----------------------------------------")
        for code, item in self.menu.items():
            print(f"[{code}]    | {item['name']:<23} | ₱{item['price']:<7.2f}")
        print("=========================================\n")

    def get_orders(self):
        while True:
            try:
                code = int(input("Enter Item Code: "))
                if code not in self.menu:
                    print("[x] Item code not found.")
                    continue

                qty = int(input("Enter Quantity: "))
                if qty <= 0:
                    print("[x] Quantity must be at least 1.")
                    continue

                item = self.menu[code]
                self.orders.append({
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": qty,
                    "line_total": item["price"] * qty
                })
                print(f"-> Added {qty}x {item['name']} to order.")

                again = input("\nWould you like to order another item? (yes/no): ").strip().lower()
                if again not in ['yes', 'y']:
                    break
            except ValueError:
                print("[x] Invalid input. Please enter numerical values.")

    def print_receipt(self):
        subtotal = sum(i["line_total"] for i in self.orders)
        discount = subtotal * 0.10 if subtotal >= 500 else 0.0
        final_total = subtotal - discount

        print("\n" + "=" * 43)
        print("               BITE & GO                 ")
        print("          OFFICIAL RECEIPT               ")
        print("=" * 43)
        for i in self.orders:
            print(f"{i['quantity']:<4} {i['name']:<20} ₱{i['price']:<7.2f} ₱{i['line_total']:<7.2f}")
        print("-" * 43)
        print(f"{'Subtotal:':<32} ₱{subtotal:>8.2f}")
        if discount > 0:
            print(f"{'Discount (10%):':<32}-₱{discount:>8.2f}")
        print(f"{'TOTAL AMOUNT DUE:':<32} ₱{final_total:>8.2f}")
        print("=" * 43 + "\n")