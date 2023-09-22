def acima_da_media(lista):
    '''...'''
    
    media=sum(lista)/len(lista)        
        
    list.sort(lista)
    ind = list.index(lista,media)
    
    fatia = lista[ind+1:]
    
    return fatia