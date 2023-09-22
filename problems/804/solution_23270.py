def filtra_pares(t):
    lista = []
    if type(t) == tuple and len(t) == 4:
        if t[0]%2 == 0:
            lista.append(t[0])
        if t[1]%2 == 0:
            lista.append(t[1])
        if t[2]%2 == 0:
            lista.append(t[2])
        if t[3]%2 == 0:
            lista.append(t[3])
    return(tuple(lista))