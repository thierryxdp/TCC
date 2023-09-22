def media_matriz(mat):
    cont = 0 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            cont = cont + mat[i][j]
            
    quantidade = len(mat) * len(mat[0])
    return round(cont/quantidade,2)