# Exercise 11
# Your solution comes here
sharings = int(input("Enter total amount of money: "))
denominations = [500, 100, 10, 5, 1]
bills_count = {}
for denom in denominations:
    num_bills = sharings // denom
    if num_bills > 0:
        bills_count[denom] = num_bills
        sharings -= num_bills * denom
output = []
for denom in [500, 100, 10, 5, 1]:
    count = bills_count.get(denom, 0)
    output.append(f"{count} ({denom})")
print(", ".join(output))