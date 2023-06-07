def calculator(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "x" or y == "X":
        return x * z
    elif y == "/":
        return x / z
    else:
        return "Invalid inputs"


def readFile(file):
    with open(file, "r") as f:
        return f.read().splitlines()
