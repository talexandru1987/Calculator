from calc import calculator, readFile


calcArray = readFile("ex1.txt")

for i in range(len(calcArray)):
    inputsArray = calcArray[i].split()
    while len(inputsArray) < 3:
        inputsArray = calcArray[int(inputsArray[1])].split()
        print(inputsArray)
