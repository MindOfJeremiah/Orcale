#imports packages 
import csv #.csv files
from datetime import date #current date
from dotenv import load_dotenv
import sys #Python system module lets you interact with the OS
import os # reads values from .gitignore

today = date.today()

load_dotenv(dotenv_path="/home/MindOfJeremiah/Desktop/orcale/.env") #loads name from .env

ALLOWED_NAME = os.getenv("ALLOWED_NAME") # ALLOWED_NAME is all caps because its a constant in python. Constants use uppercase to single this never changes

#Input section
name = input("Security first say your name and we'll start. ")
if name.lower() != ALLOWED_NAME.lower(): #.lower() converts any string to lowercase
    if ALLOWED_NAME is None:
     print("Name is not recognized, access denied.")
    sys.exit(1)  # means failure/0 everything worked
else:
    print(f"Whew, it's you {name} let's start")

income = float(input("Enter recent profit: "))
print(f"Your current is {income}")

debt = float(input("Do you have any debt? "))
if debt > 0:
    print(f"Ouch your debt is {debt}")
else: 
    print("Looks like you're debt free")

# dictionary seperates expenses by content
expenses = {
    "school": float(input("School: ")),
    "food": float(input("Food: ")),
    "bills": float(input("Bills: ")),
    "other": float(input("Other: "))
}

savings = {
    "Stocks": float(input("Stocks: ")),
    "Savings": float(input("Savings: "))
}

# Core calculations
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

#Log current entry to CSV
with open("history.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([date.today(), income, total_expenses, debt, balance, round(progress, 2)])

print (f"Progress toward Atlanta: {progress:.2f}%")

# Read history for analysis 
with open("history.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

#prints the history of the csv row by row float converts it into a .
incomes = [float(row[1]) for row in rows]
expense_history = [float(row[2]) for row in rows]
balances = [float(row[4]) for row in rows]


#divides the sum of incomes by income and expenses by expenses
avg_income = sum(incomes) /len(incomes)
avg_expenses = sum(expense_history) / len(expense_history) #columns that the .csv prints

#biggest expense from current dictonary
biggest = max(expenses, key=expenses.get)

total_savings = sum(savings.values())

trend = balances[-1] - balances[0]
if trend > 0:
    direction = "up"
else:
    direction = "down"

print(f"\n-- Oracle Analysis | {today}  ---")

print(f"Average profits:  ${avg_income:.2f}")
print(f"Baseline cost:  ${avg_expenses:.2f}")
print(f"Core Expense:  {biggest} (${expenses[biggest]:.2f})")
print(f"Net flow:  {direction}")
print(f"Available Balance:  ${balances[-1]:.2f}")
print(f"Compounding Savings: ${total_savings:.2f} ")

avg_monthly_balance = sum(balances) / len(balances)
# prints the monthly avg makes sure its greater the 0 first if not
if avg_monthly_balance > 0:
    months_to_goal = (goal - balances[-1]) / avg_monthly_balance
    print(f"At your current rate you'll reach %{goal} in: {months_to_goal:.1f} months")
else: #the if not
    print(f"At your current spending level, you will not reach your ${goal}. Your income must exceed your expenses to make progress.")