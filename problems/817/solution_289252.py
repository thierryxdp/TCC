def acima_da_media(lista):
    """..."""
    
    x = len(lista)
    y = sum(lista)
    z = y/x
    
    if z in lista:
        list.sort(lista)
        w = list.index(lista, w)
        aprovados = lista[w:]
        
        return aprovados
    
    if z not in lista:
        list.append(lista, z)
        list.sort(lista)
        w = list.index(lista, z)
        aprovados = lista[w+1:]
        
        return aprovados