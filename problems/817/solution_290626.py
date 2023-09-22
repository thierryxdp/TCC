def acima_da_media(notas):
    
    media= sum(notas)/len(notas)
	notas.append(media)
    notas.sort()
    index = notas.index(media)
    return notas[index+1:] - media