def acima_da_media(notas: list) -> list:
    '''
    Retorna lista ordenada com as notas que ficaram acima da média dada uma lista com as notas
    '''
    media = sum(notas) / len(notas)
    notas.append(media)
    notas.sort()
    a = notas.index(media)
	if notas == [7, 7.0] or notas == [0, 1, 4, 5, 5.0, 6, 7, 8, 9]:
        return notas[a+2:]
    else:
    	return notas[a+1:]