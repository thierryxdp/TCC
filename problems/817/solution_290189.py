def acima_da_media(notas):
    media_notas = sum(notas) / len(notas)
    
    if media_notas in notas:
        notas.sort()
        posicao = notas.index(media_notas)
        return notas[posicao+1:]
    else:
        notas.append(media_notas)
        notas.sort()
        posicao = notas.index(media_notas)
        return notas[posicao+1:]