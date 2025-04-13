num1 = float(input("Enter the first number: "))
opt = input("Enter Operation: ")
num2 = float(input("Enter the second number: "))

if opt == "+":
  print("Result:", num1 + num2)
elif opt == "-":
  print("Result:", num1 - num2)
elif opt == "*":
  print("Result:", num1 * num2)
elif opt == "/":
  print("Result:", num1 / num2)
else:
  print("Error")