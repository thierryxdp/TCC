def acima_da_media(notas):
    '''docs'''
    
    media = sum(notas)/len(notas)
    
    if media in notas:
        notas.sort()
        indice = notas.index(media)
        return notas[indice+1:]
    else:
        notas.insert(0, media)
        notas.sort()
        indice = notas.index(media)
        return notas[indice+1:]