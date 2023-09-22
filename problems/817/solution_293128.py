def acima_da_media(notas):
    '''teste'''

    soma_notas= sum(notas)
    media= soma_notas/(len(notas))
    list.append(notas,media)
    list.sort(notas)
    posicao=list.index(notas,media)
    x=list.count(notas,media)
    acima_media=notas[posicao+x:]

    return acima_media