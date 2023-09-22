def maiores(lista,n):
    ''' '''
    lista_ordenada=[]
    for i in lista:
        if i > n:
            lista_ordenada.append(i)
    return lista_ordenada.sort()