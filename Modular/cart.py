from config import MENU, DISCOUNT_THRESHOLD, DISCOUNT_RATE

def create_order_item(code, quantity):
    selected = MENU[code]
    return {
        "name": selected["name"],
        "price": selected["price"],
        "quantity": quantity,
        "line_total": selected["price"] * quantity
    }

def calculate_totals(orders):
    subtotal = sum(item["line_total"] for item in orders)
    discount = subtotal * DISCOUNT_RATE if subtotal >= DISCOUNT_THRESHOLD else 0.0
    final_total = subtotal - discount
    return subtotal, discount, final_total