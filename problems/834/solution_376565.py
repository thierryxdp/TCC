def media_matriz(m):
    '''Dada uma matriz, a funcao retorna a media de todos os numeros inclusos.
    list -> float'''
    divisor=len(m)*len(m[0])
    somatorio=0
    for i in range(len(m)):
		for j in range(len(m[0])):
        	somatorio+=m[i][j]
    media=somatorio/divisor
    return round(media,2)