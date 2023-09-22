def media_matriz(matriz):
    soma=0   
    valores=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma= soma+ matriz[i][j]
            valores= valores+1          
    media=soma/valores
    return round(media)