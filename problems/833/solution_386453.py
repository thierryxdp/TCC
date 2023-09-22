def conta_numero(num, mat):
    cont = 0 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat [i][j] == num:
                cont = cont+1
     
    return cont