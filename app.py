from expenses import calculate_total, filter_by_category

expenses = [
    {"name": "Lunch", "amount": 12, "category": "food"},
    {"name": "Bus", "amount": 3, "category": "transport"},
    {"name": "Coffee", "amount": 5, "category": "drinks"},
    {"name": "Dinner", "amount": 20, "category": "food"},
]

print("All expenses:")
for expense in expenses:
    print(f"- {expense['name']} | ${expense['amount']} | {expense['category']}")

total = calculate_total(expenses)
print(f"\nTotal: ${total}")

food_expenses = filter_by_category(expenses, "food")
food_total = calculate_total(food_expenses)

print("\nFood expenses:")
for expense in food_expenses:
    print(f"- {expense['name']}: ${expense['amount']}")

print(f"\nFood total: ${food_total}")