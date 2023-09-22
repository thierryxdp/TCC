def maiores(lista,n):
    """ """
    lista_saida = lista
    for i in lista:
        if n > i:
            lista_saida.append(i)
        else:
            lista_saida = []
    return lista_saida