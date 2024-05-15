# Exercise 11
# Your solution comes here
def calculation_of_bill(sharings):
    denominations = [500, 100, 10, 5, 2, 1]
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

    return ", ".join(output)

s = int(input("Enter total amount of money: "))
print(calculation_of_bill(s))