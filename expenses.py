def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def filter_by_category(expenses, category):
    filtered = []
    for expense in expenses:
        if expense["category"] == category:
            filtered.append(expense)
    return filtered