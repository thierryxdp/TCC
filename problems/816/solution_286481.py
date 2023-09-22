def maiores(lista,n):
    ''' '''
    list.sort(lista)
    lista_final= []
    for x in lista:
        if x > n:
            lista_final.append(x)
    return lista_final