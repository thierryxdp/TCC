def acima_da_media(lista):
	lista.sort()
    media = sum(lista)/len(lista)
	lista = [e for e in lista if e > media]
    return lista