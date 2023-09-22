def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    notas=notas[(notas.index(media)+1):]
    if media in notas:
        notas.remove(media)
        return notas
    else:
    	return notas