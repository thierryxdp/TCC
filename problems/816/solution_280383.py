def maiores(lista, n):
    #quant = len(lista)
    for i in lista:
        if i <= n:
            list.remove(lista, i)
    return lista