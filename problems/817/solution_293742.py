def acima_da_media(lista):
    """..."""
    
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    indice = list.index(lista,media)
    
    fatiada = [media+1:]
    
    return fatiada