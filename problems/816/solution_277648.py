def maiores(lista,n):
    """ """
    lista_saida = lista
    for i in lista:
        if n > i:
            lista_saida.append(i)
        else:
            return[]
    return lista_saida