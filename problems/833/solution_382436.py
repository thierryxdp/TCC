def conta_zeros(x):
    contador = 0
    for i in range(0,len(x)):
        for j in range(0,len(A[x])):
            if x[i][j]==0:
                contador = contador+1
    return contador