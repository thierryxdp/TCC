def conta_numero(numero: int, matriz: list) -> int:
    """ Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele número aparece na
    matriz.
    int, list(list) -> int """
    ocorrencias=0
    for i in matriz:
        for j in [matriz[i]]:
            if matriz[i][j] == numero:
                ocorrencias+=1
    return ocorrencias