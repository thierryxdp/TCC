def insere(lista_numero,n):
    '''
    '''
    lista2= lista_numero + [n]
    list.sort(lista2)
    
    p = list.index(lista2,n)
    
    return lista2[p+1:]