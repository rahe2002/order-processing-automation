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
            order["total"] = float(order["price"]) * int(order["quantity"])
            valid_orders.append(order)
        else:
            invalid_orders.append(order)

    return valid_orders, invalid_orders

def generate_report(valid, invalid):
    with open("report.txt", "w") as file:
        file.write(f"Valid orders: {len(valid)}\n")
        file.write(f"Invalid orders: {len(invalid)}\n")

        total_revenue = sum(order["total"] for order in valid)
        file.write(f"Total revenue: {total_revenue}\n")



def main():
    orders = read_orders("orders.csv")
    valid, invalid = validate_orders(orders)

    print(f"Valid orders: {len(valid)}")
    print(f"Invalid orders: {len(invalid)}")
   
    total_revenue = sum(order["total"] for order in valid)
    print(f"Total revenue: {total_revenue}")

    generate_report(valid, invalid)



if __name__ == "__main__":
    main()
