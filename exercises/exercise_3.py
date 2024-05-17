# Exercise 3
# Your solution comes here
to_be= int(input("Enter a random set of digits to be turned into time: "))
hours = (to_be // 3600) % 24
minutes = (to_be // 60) % 60
seconds = to_be % 60
time=(f"{hours}:{minutes:02d}:{seconds:02d}")
print(time)