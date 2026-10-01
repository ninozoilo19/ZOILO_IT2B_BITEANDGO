import sys
import ui
import cart


def run_pos():
    ui.print_menu()

    if not ui.get_yes_no_input("Would you like to place an order? (yes/no): "):
        print("\nThank you for visiting! Have a great day.")
        sys.exit()

    orders = []
    ordering = True

    while ordering:
        print("\n--- Add Item to Order ---")
        code = ui.get_valid_item_code()
        qty = ui.get_valid_quantity()

        item = cart.create_order_item(code, qty)
        orders.append(item)

        print(f"-> Added {qty}x {item['name']} to order.")
        ordering = ui.get_yes_no_input("\nWould you like to order another item? (yes/no): ")

    subtotal, discount, final_total = cart.calculate_totals(orders)
    ui.print_receipt(orders, subtotal, discount, final_total)


if __name__ == "__main__":
    run_pos()