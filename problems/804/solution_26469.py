def filtra_pares(a,b,c,d):
    lista = []
    if a%2 == 0:
        lista = lista + [a]
    elif b%2 == 0:
        lista = lista + [b]
    elif c%2 == 0:
        lista = lista + [c]
    elif d%2 == 0: 
        lista = lista + [d]
    return tuple(lista)