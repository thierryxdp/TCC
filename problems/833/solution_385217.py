def conta_numero(numero, matriz):
    # int, lista de lista (matriz) --> int
    num_linhas = len(matriz)
    num_vezes=0
    for i in range(0,num_linhas):
        num_colunas=len(matriz[i])
        for j in range(0,num_colunas):
            if matriz[i][j] == numero:
                num_vezes = num_vezes + 1
    return num_vezes