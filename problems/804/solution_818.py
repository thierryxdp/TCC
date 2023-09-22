def filtra_pares(tupl):
    lista1 = [tupl]
    lista2 = []
    for valor in lista1:
        if valor % 2 == 0:
            lista2.append(valor)
            print(lista2)