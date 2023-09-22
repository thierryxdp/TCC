def filtra_pares(a,b,c,d):
    lista = []
    tupla= (a,b,c,d)
    for valor in tupla:
        if valor % 2 == 0:
            lista.append(valor)
            tupla2 = tuple(lista)
            return tupla2