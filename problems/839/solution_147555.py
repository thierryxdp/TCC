def carros(Na,Ve=0):
    if Ve == 0 and Na % 5 == 0:
        return Na // 5
    else:
        return((Na // 5) + 1)
    if Ve != 0:
        return Na // Ve
    else:
        return((Na // Ve) + 1)