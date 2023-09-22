def maiores(lista, a):
    '''docs'''
    
    if a not in lista:
        lista.insert(0, a)
        
    lista.sort()
    
    indice = lista.index(a)
    
    return lista[indice+1:]