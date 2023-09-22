def conta_numero(n,matriz):
    i=(len(matriz))*2
    repeticoes=0
    
    for i in range(len(matriz)):
        for j in in range(len(matriz[i])):
            if n in matriz[i][j]:
                repeticoes=repeticoes+1
    return repeticoes