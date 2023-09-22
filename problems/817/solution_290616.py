def acima_da_media(notas):
    
    media= sum(notas)/len(notas)
	lista.append(media)
    lista.sort()
    index = lista.index(media)
    return lista[index+1:]