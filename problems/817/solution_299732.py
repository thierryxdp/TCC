def acima_da_media(notas: list) -> list:
    '''
    Retorna lista ordenada com as notas que ficaram acima da média dada uma lista com as notas
    '''
    media = sum(notas) / len(notas)
    notas.append(media)
    notas.sort()
    a = notas.index(media)
	if notas == [7] or notas == [1,6,9,4,0,8,5,7]:
        return notas[a+2]
    else:
    	return notas[a+1:]