def maiores(lista,n):
    ''' '''
    lista= list.sort(lista)
    lista_final= []
    for x in lista:
        if x > n:
            lista_final.append(x)
    return lista_final