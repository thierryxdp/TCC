def acima_da_media(notas):
    media = sum(notas)/len(notas)
    posicao = list.index(notas,media)
    if media not in notas:
        list.append(notas,media)
        list.sort(notas)
        return notas[posicao+1:]
    else:
        return notas[posicao+1:]