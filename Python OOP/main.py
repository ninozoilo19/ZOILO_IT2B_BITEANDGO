from bite_go import POSSystem


def main():
    menu_data = {
        1: {"name": "Burger Combo", "price": 120.00},
        2: {"name": "Fried Chicken w/ Rice", "price": 95.00},
        3: {"name": "Spaghetti Special", "price": 85.00},
        4: {"name": "French Fries (Large)", "price": 60.00},
        5: {"name": "Iced Tea (Regular)", "price": 35.00},
        6: {"name": "Sundaes Dessert", "price": 40.00}
    }

    pos = POSSystem(menu_data)
    pos.display_menu()

    start = input("Would you like to place an order? (yes/no): ").strip().lower()
    if start in ['yes', 'y']:
        pos.get_orders()
        pos.print_receipt()


if __name__ == "__main__":
    main()