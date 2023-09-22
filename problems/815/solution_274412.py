def insere(lista_numero, n):
    '''docs'''
    
    a = lista_numero
    
    if n > a[0]:
        return a.insert([1], n)
    elif n > a[1]:
        return a.insert(2, n)
    else:
        return