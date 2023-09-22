def conta_numero(numero,matriz):
    """funcao que conta e retorna a quantidade de vezes que o numero dado aparece na matriz"""
    """int,list->int"""
    ocorrencia = 0
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j] == numero:
        		ocorrencia = ocorrencia + 1
    return ocorrencia