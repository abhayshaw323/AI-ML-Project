data = [10, None, 20, 30, None, None, 40]

# Step 1: Count total values
total_values = len(data)

# Step 2: Count missing values (None)
missing_count = 0
for value in data:
    if value is None:
        missing_count += 1

# Step 3: Calculate percentage
percentage = (missing_count / total_values) * 100

# Step 4: Round to 2 decimal places
percentage = round(percentage, 2)

print(percentage)
