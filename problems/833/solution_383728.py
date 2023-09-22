def conta_numero(num, matriz):
    """Função que, dados um número e uma matriz (lista de lista)
    quantifique a ocorrencia desse numero na matriz
    list -> int"""
    nL = len(matriz)
    nC = len(matriz[0])
    ocorrencia = 0
    for i in range(nL):
        for j in range(nC):
            if matriz[i][j] == num:
                ocorrencia += 1
    return ocorrencia