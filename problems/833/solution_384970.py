def conta_numero(numero, matriz):
    linhas = len(matriz)
    if linhas == 0:
        return 0
    colunas = len(matriz[0])
    contagem = 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                contagem += 1
    return contagem