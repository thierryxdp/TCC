#Start your python function here
def filtra_pares(a,b,c,d):
    '''Dado uma tupla com quatro inteiros a,b,c e d, retorne somente os números pares;
    int,int,int,int -> int,...'''
    t=(a,b,c,d)
    if a%2==0:
        return a
    elif b%2==0:
        return b
    elif c%2==0:
        return c
    elif d%2==0:
        return d
    else:
        return 0
    return a+b+c+d