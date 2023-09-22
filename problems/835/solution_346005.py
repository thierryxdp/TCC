def melhor_volta(mat):
    minimo = 10000000000
    corredor = -1
    volta = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]<minimo:
                corredor = i
                volta = j
                minimo = mat[i][j]
                
    return (corredor + 1,minimo,volta+1)