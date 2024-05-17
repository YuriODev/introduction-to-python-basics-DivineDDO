# Exercise 8
# Your solution comes here
first_input= int(input())
second_input= int(input())
third_input= int(input())
small_value= min(first_input,second_input,third_input)
big_value= max(first_input,second_input,third_input)
mid_value= first_input+second_input+third_input-small_value-big_value
print(small_value)
print(mid_value)
print(big_value)