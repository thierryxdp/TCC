def carros(a,v=0):
    if v == 0 and a % 5 == 0:
        return a // 5
    if v != 0:
        return a // v
    else:
        return a // 5 + 1