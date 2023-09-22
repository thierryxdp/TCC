def insere(lista_numero, n):
    '''docs'''
    
    a = lista_numero
    b = a.insert(1, n)
    
    lista_na_ordem = b.sort()
    return lista_na_ordem