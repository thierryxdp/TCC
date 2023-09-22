def filtra_pares(t):
    tup= t
    lista = []   
    for valor in tup :
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)