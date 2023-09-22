import random
def media_matriz (matriz):
    A = []
    n = random.randint(1,10)
    
    for i in range (n):
        l = []
        for j in range (n):
            l.append(random.randint(1,10))
        A.append(l)

    soma_col_n = 0
    soma_diag = 0

    for i in range (n):
        soma_col_n += A[n-1][i]
        soma_diag += A [i][i]

        soma_acima_diag = 0
        soma_mat = 0

    for i in range(n):
        for j in range(n):
            if (j > i):
                soma_acima_diag += A[i][j]
        soma_mat += A[i][j]

    media = soma_mat / (n*n)
    return media