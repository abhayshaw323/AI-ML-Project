# Problem 1: Transaction Frequency Analyzer (User Input)

# Ask user for number of transactions
n = int(input("Enter number of transactions: "))

transactions = []

# Take transaction values from user
for i in range(n):
    amount = int(input(f"Enter transaction {i+1}: "))
    transactions.append(amount)

# Dictionary to store frequency
frequency = {}

for amount in transactions:
    if amount in frequency:
        frequency[amount] += 1
    else:
        frequency[amount] = 1

# Sort by frequency (descending) and value (ascending)
sorted_transactions = sorted(
    frequency.items(),
    key=lambda x: (-x[1], x[0])
)

# Display top 2 frequent transactions
print("Top 2 frequent transactions:",
      [sorted_transactions[0][0], sorted_transactions[1][0]])

# Problem 2: Missing Value Percentage Calculator (User Input)

# Ask user for number of values
n = int(input("\nEnter number of data values: "))

data = []

print("Enter values (type 'None' for missing value):")

for i in range(n):
    value = input(f"Enter value {i+1}: ")
    if value == "None":
        data.append(None)
    else:
        data.append(int(value))

# Count missing values
total = len(data)
missing = 0

for value in data:
    if value is None:
        missing += 1

# Calculate percentage
percentage = round((missing / total) * 100, 2)

print("Missing value percentage:", percentage)
