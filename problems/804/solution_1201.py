#Start your python function here
def filtra_pares(a,b,c,d):
    '''Dado uma tupla com quatro inteiros a,b,c e d, retorne somente os números pares;
    int,int,int,int -> int,...'''
    t=(a,b,c,d)
    if t[0]%2==0:
        return a
    elif t[1]%2==0:
        return b
    elif t[2]%2==0:
        return c
    elif t[3]%2==0:
        return d
    else:
        return
    return a+b+c+d