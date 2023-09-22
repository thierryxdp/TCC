def conta_numero(numero, matriz):
    ap = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                ap = ap+1
                
    return ap