def filtra_pares(t):
    lista = [0:]    
    for valor in tuple(t):
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)