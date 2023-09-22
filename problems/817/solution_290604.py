def acima_da_media(notas):
    notas.sort()
	notas.append(media)

    media= sum(notas)/len(notas)
    index= notas.index(media)
    return notas[index+1:]