def acima_da_media(lista):
    media=sum((lista[:])/len(lista))
    posicao=list.index(lista,media)
    list.sort(lista)
    return lista[posicao::]