def filtra_pares(t):
    lista = []
    for sub in t:
        if sub%2==0:
            lista.append(sub)
            return tuple(lista)