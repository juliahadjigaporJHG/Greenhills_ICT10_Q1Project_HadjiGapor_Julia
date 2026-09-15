from pyscript import document


def generate_sku(event):

    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    stock = document.querySelector("#stock").value

    category = category.strip()
    product = product.strip()

    if not category or not product or not stock:
        document.querySelector("#show").innerText = "Please fill in all fields."
        return

    category_code = category[:3].upper()
    product_code = product[:3].upper()

    sku = f"{category_code}-{product_code}-{stock}"

    document.querySelector("#show").innerText = f"SKU: {sku}"


def create_order(event):

    total = 0
    order = []

    dcc = document.querySelector("#dcc")
    dccm = document.querySelector("#dccm")
    dccb = document.querySelector("#dccb")

    if dcc.checked:
        total += int(dcc.value)
        order.append("Dubai Chewy Cookie - ₱159")

    if dccm.checked:
        total += int(dccm.value)
        order.append("Dubai Chewy Cookie Matcha - ₱179")

    if dccb.checked:
        total += int(dccb.value)
        order.append("Dubai Chewy Cookie Biscoff - ₱199")

    if not order:
        document.querySelector("#show").innerText = "Please select an item."
        return

    result = "ORDER\n\n"

    for item in order:
        result += item + "\n"

    result += f"\nTOTAL: ₱{total}"

    document.querySelector("#show").innerText = result
