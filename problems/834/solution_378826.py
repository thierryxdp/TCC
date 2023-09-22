def media_matriz(matriz:list)->int:
    x=0
    y=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
        	y=y+1
        	x=x+matriz[i][j]
    return x/y