transactions = [200, 500, 200, 100, 500, 200, 100, 500, 500]

# Step 1: Create an empty dictionary to store frequency
frequency = {}

# Step 2: Count how many times each transaction appears
for amount in transactions:
    if amount in frequency:
        frequency[amount] += 1
    else:
        frequency[amount] = 1

# Step 3: Sort the dictionary items
# First by frequency (descending), then by value (ascending)
sorted_transactions = sorted(
    frequency.items(),
    key=lambda x: (-x[1], x[0])
)

# Step 4: Extract the top 2 transaction amounts
result = [sorted_transactions[0][0], sorted_transactions[1][0]]

print(result)
