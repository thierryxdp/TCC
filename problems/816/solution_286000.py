def maiores(lista,n):
    ''' '''
    lista_ordenada=[]
    for i in lista:
        if i > n:
            lista_ordenada.append(i)
            lista_ordenada.sort()
    return lista_ordenada