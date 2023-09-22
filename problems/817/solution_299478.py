def media(notas):
    return sum(notas) // len(notas)
	
def acima_da_media(notas):
    notas.append(media(notas))
    notas.sort()
    return notas[notas.index(media(notas))+1:len(notas)]