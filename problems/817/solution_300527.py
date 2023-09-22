def acima_da_media(lista,n):

    list.append(lista,n)
    list.sort(lista)
    g=list.index(lista,n)
    return lista[g+1: ]
    media= sum(lista)/len(lista)
if media in lista:
    
    return acima_da_media(media,lista)[1: ]
    
else:
    return acima_da_media(media,lista)