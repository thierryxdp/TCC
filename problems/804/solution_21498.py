def filtra_pares(t):
    lista = []    
    for valor in tuple(t):
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)