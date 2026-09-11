from pyscript import display, document

PRICES = {
    "c1": 180.00,
    "c2": 160.00,
    "c3": 180.00,
    "c4": 175.00,
    "c5": 175.00,
}

TAX_RATE = 0.12

def create_order(e):
    subtotal = 0.0

    for item_id, price in PRICES.items(): 
        if document.getElementById(item_id).checked: 
            subtotal += price

    tax = subtotal * TAX_RATE 
    total = subtotal + tax


    receipt_div = document.getElementById("receipt")
    receipt_div.innerHTML = "<h2>==== Receipt ====</h2>"

    display(f"Subtotal: ₱{subtotal:.2f}", target="receipt")
    display(f"Tax (12%): ₱{tax:.2f}", target="receipt") 
    display(f"Total: ₱{total:.2f}", target="receipt")
