def conta_numero(n,matriz):
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if n == matriz[i][j]:
                cont +=1
    return cont