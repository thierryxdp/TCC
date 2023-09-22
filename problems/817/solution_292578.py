def acima_da_media(notas):
    '''função que retorna uma lista ordenada com as notas
       que ficaram acima da média'''
    media=sum(notas)/len(notas)
    notas.sort()
    if media in notas:
        indice=notas.index(media)
        return notas[indice+1:]
    else:
        notas.append(media)
        notas.sort()
        indice=notas.index(media)
        return notas[indice+1:]