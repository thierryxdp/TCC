#retorna apenas os numeros pares
#tupla->tupla

def af(a):
    if (a%2)!=0:
        return [ ]
    else:
        return [a]
def bf(b):
    if (b%2)!=0:
        return [ ]
    else:
        return [b]
def cf(c):
    if (c%2)!=0:
        return [ ]
    else:
        return [c]
def df(d):
    if (d%2)!=0:
        return [ ]
    else:
        return [d]
def filtra_pares (x):
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    return af(a)+bf(b)+cf(c)+df(d)