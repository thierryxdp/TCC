def conta_numero(numero, matriz):
    # int, lista de lista (matriz) --> int
    num_linhas = len(matriz)
    num_vezes=0
    for i in range(0,num_linhas):
        for j in range(0,len(matriz[i]):
            if matriz[i][j] == numero:
               num_vezes = num_vezes + 1
    return num_vezes