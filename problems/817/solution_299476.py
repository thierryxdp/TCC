def media(notas):
    return sum(notas) // len(notas)
	
def acima_da_media(notas):
    notas.append(media(notas))
    notas.sort()
    return notas.index(media(notas))