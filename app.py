from expenses import calculate_total

expenses = [
    {"name": "Lunch", "amount": 12},
    {"name": "Bus", "amount": 3},
    {"name": "Coffee", "amount": 5},
]

print("Expenses:")
for expense in expenses:
    print(f"- {expense['name']}: ${expense['amount']}")

total = calculate_total(expenses)
print(f"\nTotal: ${total}")