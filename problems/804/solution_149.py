def filtra_pares(tupla):
    pares = []
    for valor in tupla:
        if valor % 2 == 0:
            pares.append(valor)
            print pares