def conta_numero(n,matriz):
    i=(len(matriz))*2
    repeticoes=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if n == matriz[i][j]:
                repeticoes=repeticoes+1
    return repeticoes