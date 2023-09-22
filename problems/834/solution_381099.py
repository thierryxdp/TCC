def media_matriz(matriz):
    c=0
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            soma=soma+matriz[i][j]
    return round(s/c,2)