#Start your python function here
def filtra_pares(a,b,c,d):
    """retorna uma tupla par dados 2 tuplas"""
    if a%2==0 and b%2==0:
        return a,b
    elif a%2==0 and c%2==0:
        return a,c
    elif a%2==0 and d%2==0:
        return a,d
    elif b%2==0 and c%2==0:
        return b,c
    elif b%2==0 and d%2==0:
        return b,d
    elif c%2==0 and d%2==0:
        return c,d