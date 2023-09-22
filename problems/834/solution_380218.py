def media_matriz(matriz):
    total=0
    mediador=0
    for i in range(len(matriz)):
        mediador=mediador+len(matriz[i])
    	for j in range(len(matriz[i])):
            total=total+matriz[i][j]
    return round(total/mediador,2)