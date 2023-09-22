def filtra_pares(a,b,c,d):
    e = a,b,c,d
    lista1 = list(e)
    lista2 = []
    for valor in lista1:
        if (valor % 2) == 0:
            lista2.append(valor)     
    return lista2