def acima_da_media(notas):
    notas.sort()
    media= sum(notas)/len(notas)
    notas.append(media)
    index= notas.index(media)
    return [index+1:]