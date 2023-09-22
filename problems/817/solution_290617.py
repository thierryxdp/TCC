def acima_da_media(notas):
    
    media= sum(notas)/len(notas)
	notas.append(media)
    notas.sort()
    index = lista.index(media)
    return lista[index+1:]