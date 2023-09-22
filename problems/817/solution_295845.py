def acima_da_media(notas):
    soma = sum(notas)
    media = soma/len(notas)
    notas.append(media)
    notas.sort()
    posicao = notas.index(media)
    if notas[posicao+1] == media:
        return notas[posicao+2:]
    else:
        return notas[posicao+1:]