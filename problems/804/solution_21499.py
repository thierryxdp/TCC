def filtra_pares(t):
    lista = [] 
    lista1 = t
    for valor in lista1 :
        if valor % 2 == 0:
            lista.append(valor)
            return tuple(lista)