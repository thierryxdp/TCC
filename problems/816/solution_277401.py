def maiores(listaint,n):
    ''' '''
    lista = listaint + [n] 
    list.sort(lista)
    x = list.imdex(lista,n)
    y = list.count(lista,n)
    return lista[x + y:]