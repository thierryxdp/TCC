def maiores(lista_numero,n):
    ''' '''
    lista = lista_numero + [n] 
    list.sort(lista)
    x = list.index(lista,n)
    y = list.count(lista,n)
    
    return lista[x + y:]