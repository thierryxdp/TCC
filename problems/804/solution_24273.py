def filtra_pares(T):
    lista_T = []
    for n in T:
        if n%2 == 0:
            lista_T.append(n)
    return tuple(lista_T)