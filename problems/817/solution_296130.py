def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    
    list.sort(lista)
    lista= lista[:media]
    
    return lista