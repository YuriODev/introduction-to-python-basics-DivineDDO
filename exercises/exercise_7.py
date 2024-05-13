# Exercise 7
# Your solution comes here
number=int(input("Enter a four digit number:"))
thousands_digit = number // 1000
hundreds_digit = (number % 1000) // 100
tens_digit = (number % 100) // 10
units_digit = number % 10
sum_of_digits = thousands_digit + hundreds_digit + tens_digit + units_digit
print(sum_of_digits)