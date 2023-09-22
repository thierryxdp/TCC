def acima_da_media(lista):
    
    i = len(lista)
    list.sort(lista)
    media = int(sum(lista)//i)
    media_total = list.index(lista,media) 
    
    if (media_total in lista):
        return lista[media_total+1:]
    else:
        return lista[media:]