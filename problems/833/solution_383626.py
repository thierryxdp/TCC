def conta_numero(numero, matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    contador = 0
    for i in range(0, n_linhas):
        for j in range(0, n_colunas):
            if(numero == matriz[i][j]):
                contador = contador + 1
    return contador