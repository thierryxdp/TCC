def maiores(lista, n):
    '''---'''
    
    if n not in lista:
        list.append(lista, n)
        
    list.sort(lista)
    indice = list.index(lista, n)
    
    fatiamento = lista[indice+1:]
    
    return fatiamento