expenses = []
print("Expense Tracker")

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    expenses.append([category, amount])

    print("Expense added:", category, "-", amount)

    choice = input("Add another expense? (yes/no): ")

    if choice.lower() == "no":
        break

print("\nYour expenses:")

total = 0

for item in expenses:
    category = item[0]
    amount = item[1]

    print(category, "₹", amount)

    total = total + amount

print("\nTotal expenses: ₹", total)