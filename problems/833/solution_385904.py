def conta_numero(numero,matriz):
    vezes=0
    for i in range(matriz):
        for j in range(matriz[0]):
            if numero==matriz[i][j]:
                vezes+=1
    return vezes