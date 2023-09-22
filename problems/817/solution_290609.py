def acima_da_media(notas):
    notas.sort()

    media= sum(notas)/len(notas)
    index= notas.index(media)
	notas.append(media)

    return notas[index+1:]