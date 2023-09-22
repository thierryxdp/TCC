def carros(a,v=0):
    if v == 0 and a % 5 == 0:
        return a // 5
    elif v != 0 and a%5==0:
        return a // v