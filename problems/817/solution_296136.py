def acima_da_media(lista):
    
    list.sort(lista)
    
    
    media=sum(lista)//len(lista)
    
    lista= lista[media:]
    return lista