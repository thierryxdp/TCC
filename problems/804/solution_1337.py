def filtra_pares(lista):
    """filtra os elementos pares de uma lista"""
    lista1 = [lista]
    lista2 = []
    for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)
        return lista2