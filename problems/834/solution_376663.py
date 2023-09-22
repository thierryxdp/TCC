def media_matriz(matriz):
    total=0
    zeros=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            total=total+1
            if matriz[i][j]==0:
                zeros=zeros+1
    return round(((total -zeros)/total),2)