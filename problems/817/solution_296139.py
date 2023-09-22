def acima_da_media(lista):
    
    list.sort(lista)
    list.reverse(lista)
    
    
    media=round(sum(lista)/len(lista))
    
    lista= lista[media:]
    list.sort(lista)
    return lista