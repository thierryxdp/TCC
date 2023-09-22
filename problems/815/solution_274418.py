def insere(lista_numero, n):
    '''docs'''
    
    a = lista_numero
    b = n

    a.append(b)
    
    lista_na_ordem = a.sort()
    return lista_na_ordem