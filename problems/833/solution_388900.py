def conta_numero(numero,matriz):
    """Funcao recebe uma matriz e retorna quantas vezes o numero aparece na matriz
    int , list -> int"""
    ocorrencia = 0
    for i in range(len(matriz)):
        for b in range(len(matriz[i])):
            if matriz[i][b] == numero:
                ocorrencia += 1
    return ocorrencia