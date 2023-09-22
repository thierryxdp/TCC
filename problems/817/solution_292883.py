def acima_da_media(lista):
    media=(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    posicao=(list.index(lista,media)+1)
    
    if int(media) in lista:
        return lista[posicao+1:]
    else:
    return lista[posicao:]