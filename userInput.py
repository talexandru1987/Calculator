from calc import calculator

firstNum = int(input("Please enter the first number: "))

secondNum = int(input("Please enter the second number: "))

operator = input("Please enter the operator (x, +, -, /): ")

print(calculator(firstNum, operator, secondNum))
