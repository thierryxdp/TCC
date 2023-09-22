def carros(a, b=5):
    if a % b != 0:
        return a//b + 1
    else:
        return a//b