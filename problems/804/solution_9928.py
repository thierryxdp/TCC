def filtra_pares(a,b,c,d):
    '''Dada uma tupla de 4 números inteiros, retorna a mesma somente com os números pares'''
    r=()
    if a%2==0:
        r=(a)
    elif b%2==0:
        r=(a,b)
    elif c%2==0:
        r=(a,b,c)
    elif d%2==0:
        r=(a,b,c,d)
    return r()