# Exercise 9
# Your solution comes here
h = int(input("Enter the number of hours passed (0 < h < 12): "))
m = int(input("Enter the number of minutes passed (0 <= m < 60): "))
s = int(input("Enter the number of seconds passed (0 <= s < 60): "))
if h == 12:
    h = 0
seconds_passed = h * 3600 + m * 60 + s
proportion = seconds_passed / (12 * 3600)
angle = proportion * 360
print(angle)