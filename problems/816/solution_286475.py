def maiores(lista,n):
    ''' '''
    lista_final= []
    for x in lista:
        if x > n:
            lista_final.append(x)
    return  list.sort(lista_final)