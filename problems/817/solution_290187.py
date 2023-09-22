def acima_da_media(notas):
    media_notas = sum(notas) / len(notas)
    
    if media_notas in notas:
        notas.sort()
        posicao = notas.index(media_notas)
        return notas[posicao+1:]
    else:
        lista.append(media)
        lista.sort()
        posicao=lista.index(media)
        return lista[posicao+1:]