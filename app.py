import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sample_expenses.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Group by Category
category_total = df.groupby("Category")["Amount"].sum()

# Print summary
print("Category Wise Spending:")
print(category_total)

# Pie Chart
plt.figure()
category_total.plot(kind="pie", autopct="%1.1f%%")
plt.title("Expense Distribution by Category")
plt.ylabel("")
plt.show()

# Monthly spending
df["Month"] = df["Date"].dt.month
monthly_total = df.groupby("Month")["Amount"].sum()

plt.figure()
monthly_total.plot(kind="bar")
plt.title("Monthly Expense")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.show()

# Budget Alert Example
food_budget = 500
food_spent = category_total.get("Food", 0)

if food_spent > food_budget:
    print("⚠ Warning: Food budget exceeded!")
else:
    print("Food budget under control.")
    total_spending = df["Amount"].sum()
print("\nTotal Spending:", total_spending)
total_spending = df["Amount"].sum()
print("\nTotal Spending:", total_spending)