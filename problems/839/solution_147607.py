def carros(a,v=0):
    if v == 0 and a % 5 == 0:
        return a // 5
    if v == 0 and a % 5 != 0:
        return a // 5 + 1
    if v != 0:
        return a // v
    if v!= 0 and a % v != 0:
        return a // v + 1