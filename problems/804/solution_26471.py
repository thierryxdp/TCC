def filtra_pares(a):
    lista = []
    a = list(a)
    if a[0]%2 == 0:
        lista = lista + a[0]
    elif a[1]%2 == 0:
        lista = lista + a[1]
    elif a[2]%2 == 0:
        lista = lista + a[2]
    elif a[3]%2 == 0: 
        lista = lista + a[3]
    return tuple(lista)