def acima_da_media(lista):
    numero_elem=len(lista)
    media=(sum(lista))/numero_elem
    posicao=list.index(lista,media)
    list.sort(lista)
    return lista[posicao::]