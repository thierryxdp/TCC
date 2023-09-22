def acima_da_media(lista):
    '''...'''
    
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    indice = list.index(lista,media)
    
    fatia = [media+1:]
    
    return fatia