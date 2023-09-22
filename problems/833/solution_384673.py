def conta_numero(n,matriz):
    i = 0
    c = 0
    for i in range(len(matriz)):
        j = 0
        for j in range(len(matriz[i])):
           if n == matriz[i][j]:
               c = c + 1 
    return c