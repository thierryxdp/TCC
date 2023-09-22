def conta_numero(numero,matriz):
    """funcao que conta e retorna a quantidade de vezes que o numero dado aparece na matriz"""
    """int,list->int"""
    ocorrencia = 0
    for linha in len(matriz):
        for coluna in len(matriz[0]):
            if matriz[linha][coluna] == numero:
        		ocorrencia = ocorrencia + 1
    return ocorrencia