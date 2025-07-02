input_list = [1, 2, 4, 6, 7]
missing = []

# Step 1: Find min and max manually
min_val = input_list[0]
max_val = input_list[0]

for num in input_list:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

# Step 2: Check each number in the range
for i in range(min_val, max_val + 1):
    found = False
    for num in input_list:
        if i == num:
            found = True
            break
    if not found:
        missing.append(i)

# Step 3: Print missing elements
print("Missing elements:", missing)
