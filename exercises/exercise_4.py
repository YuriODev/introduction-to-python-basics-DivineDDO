# Exercise 4
# Your solution comes here
symmetry= int(input("Enter a four digit number: "))
if symmetry>9999 or symmetry<1000:
  print("The number entered is not four digits")
else:
  print("Entered number is four digits now checking for symmetry")
checkings=str(symmetry)
if checkings[0]==checkings[3] and checkings[1]==checkings[2]:
  print(1)
else:
  print(0)