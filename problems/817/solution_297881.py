def acima_da_media(lista):
    
    i = len(lista)
    list.sort(lista)
    media = int(sum(lista)//i)
    
    if (media in lista):
        media_total = list.index(lista,media)    
        return lista[media_total+1:]
    else:
        return lista[:media]