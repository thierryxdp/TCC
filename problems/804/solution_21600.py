def filtra_pares(t):
    lista = []
    lista3=t
    for sub in lista3:
        if sub%2==0:
            lista.append(sub)
            return tuple(lista)