def media_matriz(mat):
   	media = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            media = media + numeros[i][j]
    m = media/(len(mat))
    return m