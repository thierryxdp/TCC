def media_matriz(matriz:list)->int:
    x=0 #acumulador
    y=0 #contador
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
        	y=y+1
        	x=x+matriz[i][j]
    return round(x/y,2)