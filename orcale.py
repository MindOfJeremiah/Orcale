import csv
from datetime import date

name = input("How are you Digit? ")
print(f"Ready to work {name}")

income = float(input("Enter recent income: "))
print(f"Your income is {income}")

debt = float(input("Got any debt? "))
print(f"Ouch your debt is {debt}")

expenses = {
    "school": float(input("School: ")),
    "food": float(input("Food: ")),
    "bills": float(input("Bills: ")),
    "other": float(input("Other: "))
}
total_expenses =sum(expenses.values())
print(f"Total expenses: ${total_expenses}")

def calculate_balance(income, total_expenses, debt):
    balance = income - total_expenses - debt
    return balance 

goal = 9000
balance = calculate_balance(income, total_expenses, debt)
progress = (balance / goal) * 100 #calculations

print(f"Balance: ${balance}")
print(f"Goal: ${goal}")
print(f"Remaining: ${goal - balance}") # Results

with open("history.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([date.today(), income, total_expenses, debt, balance, round(progress, 2)])

with open("history.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print (f"Progress toward Atlanta: {progress:.2f}%")