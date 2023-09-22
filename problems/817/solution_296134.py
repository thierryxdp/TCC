def acima_da_media(lista):
    
    list.sort(lista)
    list.reverse(lista)
    
    media=sum(lista)/len(lista)
    
    lista= lista[0:media]
    return lista