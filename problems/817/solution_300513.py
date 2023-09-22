def acima_da_media(lista,n):
    #def maiores(lista,n)
    list.append(lista,n)
    list.sort(lista)
    g=list.index(lista,n)
    return lista[g+1: ]
    media= sum(lista)/len(lista)
    if media in lista:
    h=maiores(media,lista)
    return h[1: ]
    else
    return maiores(lista ,media)