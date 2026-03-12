#imports packages 
import csv #.csv files
from datetime import date #current date

#Input uses the data to calculate the income, debt, and name
name = input("How are you Digit? ")
print(f"Ready to work {name}")

income = float(input("Enter recent income: "))
print(f"Your income is {income}")

debt = float(input("Got any debt? "))
print(f"Ouch your debt is {debt}")

# dictionary seperates expenses by content
expenses = {
    "school": float(input("School: ")),
    "food": float(input("Food: ")),
    "bills": float(input("Bills: ")),
    "other": float(input("Other: "))
}
#adds up the total sum
total_expenses = sum(expenses.values())
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

#pulls current date writes into a .csv to Log
with open("history.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([date.today(), income, total_expenses, debt, balance, round(progress, 2)])

#prints to a new row within the .csv
with open("history.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print (f"Progress toward Atlanta: {progress:.2f}%")

with open("history.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

incomes = [float(row[1]) for row in rows]
expenses = [float(row[2]) for row in rows]
balances = [float(row[4]) for row in rows]

avg_income = sum(incomes) /len(incomes)
avg_expenses = sum(expenses) / len(expenses)

trend = balances[-1] - balances[0]
if trend > 0:
    direction = "up"
else:
    direction = "down"

print(f"\n-- Orcale Anaylsis ---")
print(f"Average income: ${avg_income:.2f}")
print(f"Average expenses: ${avg_expenses:.2f}")
print(f"Balance trend: {direction}")
print(f"Latest balance: ${balances[-1]:.2f}")

avg_monthly_balance = sum(balances) / len(balances)

if avg_monthly_balance > 0:
    months_to_goal = (goal - balances[-1]) / avg_monthly_balance
    print(f"At your current rate you'll reach %{goal} in: {months_to_goal:.1f} months")
else:
    print(f"At this rate you will not reach your ${goal} - your income must exceed expenses")