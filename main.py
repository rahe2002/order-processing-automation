import csv

def read_orders(file_name):
    orders = []
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(row)
    return orders

def validate_orders(orders):
    valid_orders = []
    invalid_orders = []

    for order in orders:
        if order["customer"] and order["price"]:
            valid_orders.append(order)
        else:
            invalid_orders.append(order)

    return valid_orders, invalid_orders

def main():
    orders = read_orders("orders.csv")
    valid, invalid = validate_orders(orders)

    print(f"Valid orders: {len(valid)}")
    print(f"Invalid orders: {len(invalid)}")

if __name__ == "__main__":
    main()
