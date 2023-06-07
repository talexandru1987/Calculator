from calc import calculator, readFile

calcArray = readFile("ex.txt")
total = 0


for i in range(len(calcArray)):
    inputsArray = calcArray[i].split()
    rezult = calculator(int(inputsArray[2]), inputsArray[1], int(inputsArray[3]))
    total += rezult

print(f"The total rezult is: {total}")
