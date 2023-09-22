def filtra_pares(t):
    lista = []
    for valor in t[0:]:
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)