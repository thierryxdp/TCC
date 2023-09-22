def filtra_pares(tupla):
    lista_completa = (tupla)
    lista_pares = []
    for x in lista_completa:
        if x % 2 == 0:
            lista_pares.append(x)
            return lista_pares