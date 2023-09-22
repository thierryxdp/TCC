def filtra_pares(a, b, c, d):
    tupla = (a, b, c, d)
    lista = list()
    for i in tupla:
        if tupla[i-1] % 2 == 0:
            lista.append(tupla[i-1])
    tupla2 = tuple(lista)
    print(tupla2)