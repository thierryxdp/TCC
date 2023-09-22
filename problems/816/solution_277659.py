def maiores(lista,n):
    """ """
    lista_saida = []
    for i in lista:
        if n < i:
            lista_saida.append(i)
    lista_saida.sort()
    return lista_saida