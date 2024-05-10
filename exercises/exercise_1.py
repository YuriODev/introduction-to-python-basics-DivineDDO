# Exercise 1
# Your solution comes here
five_digits= str(input("Enter a five digit number but it would be a string store: "))
interger=int(five_digits)
first_side= ((interger//10000)%10) + ((interger//100)%10) + ((interger//1)%10)
second_side= ((interger//1000)%10) + ((interger//10)%10)
new_number= (str(first_side))+(str(second_side))
print(new_number)