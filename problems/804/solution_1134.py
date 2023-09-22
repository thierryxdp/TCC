def filtra_pares(a,b,c,d):
    """filtra os números pares de uma lista"""
    lista1 = [1,2,3,4]
    lista2 = []
    for valor in lista1:
        if valor%2==0:
            lista2.append(valor)
            return lista2