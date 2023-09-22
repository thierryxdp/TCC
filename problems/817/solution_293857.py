def acima_da_media(lista,x):
    '''...'''
    
    media=sum(lista)/len(lista)        
        
    list.sort(lista)
    
    indice = list.index(lista,x)
    
    fatia = lista[indice+1:]
    
    return fatia