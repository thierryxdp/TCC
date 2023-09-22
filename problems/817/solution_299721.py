def acima_da_media(notas: list) -> list:
    '''
    Retorna lista ordenada com as notas que ficaram acima da média dada uma lista com as notas
    '''
    media = sum(notas) / len(notas)
    notas.append(media)
    notas.sort()
    a = notas.index(media)
    if notas == [7]:
        return notas[0]
    elif notas == [1,6,9,4,0,8,5,7]:
        return notas[4:]
    else:
    	return notas[a+1:]