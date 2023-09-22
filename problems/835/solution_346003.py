def melhor_volta(mat):
    minimo = 10000000000
    corredor = -1
    tempo = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]<minimo:
                corredor = i
                minimo = j
                tempo = mat[i][j]
                
    return (corredor + 1,tempo,j+1,)