def acima_da_media(notas):
    soma = sum(notas)
    media = soma/len(notas)
    notas.append(media)
    notas.sort()
    posicao = notas.index(media)
    return notas[posicao+1:]