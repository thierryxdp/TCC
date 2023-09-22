def maiores(lista,n):
    """ """
    lista_saida = list    
    for i in lista:
        if n > lista[i]:
            lista_saida.append(lista[i])
    return lista_saida