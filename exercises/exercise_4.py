# Exercise 4
# Your solution comes here
symmetry= int(input("Enter a four digit number: "))
if symmetry>9999 or symmetry<1000:
  print("The number entered is not four digits")
else:
  print("Entered number is four digits now checking for symmetry")
str(symmetry)
if symmetry[0]==symmetry[3] and symmetry[1]==symmetry[2]:
  print(1)
else:
  print(0)