tupla = (a,b,c,d)

def pares(value):
    return value%2==0

def filtra_pares(tupla):
    return list(filter(pares,lista))