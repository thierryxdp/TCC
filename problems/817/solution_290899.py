def acima_da_media(notas):
    
    media= sum(notas)/len(notas)
    if media in notas:
        notas.remove(media)
    notas.append(media)
    notas.sort()
    index = notas.index(media)
    return notas[index+1:]