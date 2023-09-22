def filtra_pares(lista1):
    "filtra os números pares de uma tupla"
    lista2=[()]
    for valor in lista1:
        if valor % 2 == 0:
            lista2.append(valor)
    return (lista2)