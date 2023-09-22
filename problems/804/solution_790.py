def filtra_pares(tupla):
    lista_completa = (tupla)
    lista_pares = []
    for valor in lista_completa:
        if valor % 2 == 0:
            lista_pares.append(valor)
            return lista_pares