def media_matriz(matriz):
    '''
    Funçao eu recebe uma matriz e retorna a media
    de todos os numero dessa matriz
    list -> float
    '''
    a=len(matriz)
    b=len(matriz[0])
    d=a*b
    media=0
    for i in matriz:
        for j in matriz:
            media+=j
	return round(media/d,2)