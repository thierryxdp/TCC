def filtra_pares(a):
    lista1 = list(a)
    lista2 = []
    for valor in lista1:
        if (valor % 2) == 0:
            lista2.append(valor)     
    return tuple(lista2)