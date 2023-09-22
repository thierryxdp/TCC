def filtra_pares(a,b,c,d):
    """ """
    lista = [a,b,c,d]
    listPar = []
    for valor in lista:
        if valor % 2 == 0:
            listaPar.append (valor)
    return listaPar