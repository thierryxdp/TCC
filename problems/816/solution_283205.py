def maiores(x,n):
    lista = []
    if x[0] > n:
        lista = lista + [x[0]]
    elif x[1] > n:
        lista = lista + [x[1]]
    return lista