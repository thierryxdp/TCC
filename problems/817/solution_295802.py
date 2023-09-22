def acima_da_media(notas):
    media = sum(notas)/len(notas)
    if media not in notas:
        list.append(notas,media)
        list.sort(notas)
        posicao = list.index(notas,media)
        return notas[posicao+1:]
    else:
        list.sort(notas)
        posicao = list.index(notas,media)
        return notas[posicao+1:]