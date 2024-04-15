def print_orders(orders):
    for i, order in enumerate(orders, start=1):
        customer_name, product, quantity = order
        print(f"Order {i}:")
        print(f"Customer Name: {customer_name}")
        print(f"Product: {product}")
        print(f"Quantity: {quantity}\n")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Print order details
print_orders(orders)