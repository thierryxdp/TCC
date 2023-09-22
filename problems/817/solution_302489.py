def acima_da_media(notas):
    if(len(notas)==1):
    	return []
    else:
        media=sum(notas)/len(notas)
        notas.append(media)
        notas.sort()
        return notas[notas.index(media)+1:]