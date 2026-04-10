def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total