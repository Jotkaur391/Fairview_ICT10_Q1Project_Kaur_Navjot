from pyscript import document

# ================= Menu and prices =================
menu_prices = {
    "Chestnut Ice Cream": 100,
    "Makgeolli Ice Cream": 120,
    "Corn Ice Cream": 90,
    "Green Tea Ice Cream": 110,
    "Sweet Potato Ice Cream": 130
}

# ================= Order Computation =================
def compute_order(event):
    name = document.getElementById("cust_name").value or "Unknown"
    address = document.getElementById("cust_address").value or "N/A"
    contact = document.getElementById("cust_contact").value or "N/A"

    selected_items = []
    total = 0

    for i, item in enumerate(menu_prices.keys(), start=1):
        if document.getElementById(f"item{i}").checked:
            selected_items.append(item)
            total += menu_prices[item]

    items_str = "\n".join(f"🍦 {item} - ₱{menu_prices[item]}" for item in selected_items) if selected_items else "No items selected."

    summary_text = f"""📝 Order Summary:
👤 Customer Name: {name}
🏠 Address: {address}
📞 Contact: {contact}

🍨 Ordered Items:
{items_str}

💰 Total Amount: ₱{total}
"""
    document.getElementById("summary").innerText = summary_text

# ================= Navbar Section Switching =================
def show_home(event):
    document.getElementById("home-section").style.display = "block"
    document.getElementById("order-section").style.display = "none"
    document.getElementById("contact-section").style.display = "none"

def show_order(event):
    document.getElementById("home-section").style.display = "none"
    document.getElementById("order-section").style.display = "block"
    document.getElementById("contact-section").style.display = "none"

def show_contact(event):
    document.getElementById("home-section").style.display = "none"
    document.getElementById("order-section").style.display = "none"
    document.getElementById("contact-section").style.display = "block"
