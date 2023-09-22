def carros(a,v=0):
    if v == 0 and a % 5 == 0:
        return a // 5
    if v > 0:
        return a // v 
    if a % v != 0:
        return a // v + 1
    else:
        return a // 5 + 1