def filtra_pares(tupla):
    lista_completa = (tupla)
    lista_pares = []
    for c in lista_completa:
        if c % 2 == 0:
            lista_pares.append(c)
            print(lista_pares)