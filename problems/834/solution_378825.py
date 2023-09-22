def media_matriz(matriz:list)->int:
    x=0
    y=0
    for i in range(matriz):
        for j in range(matriz[i]):
        	y=y+1
        	x=x+matriz[i][j]
    return x/y