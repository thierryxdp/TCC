def conta_numero(numero, matriz):
    lin = len(matriz)
    col = len(matriz[0])
    qtd = 0
    for i in range (0, lin):
        for c in range(0, col):
            if numero == matriz[i][c]:
                qtd +=1
    return qtd