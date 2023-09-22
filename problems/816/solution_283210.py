def maiores(x,n):
    lista = []
    if x[0] > n:
        lista = lista + [x[0]]
    elif x[1] > n:
        lista = lista + [x[1]]
    elif x[2] > n:
        lista = lista + [x[2]]
    elif x[3] > n:
        lista = lista + [x[3]]
    else:
        lista = []
    return lista