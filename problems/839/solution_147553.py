def carros(Na):
    if Na % 5 == 0:
        return Na // 5
    else:
        return((Na // 5) + 1)