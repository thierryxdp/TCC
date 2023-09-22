def conta_numero(numero,matriz):
    """Pede um número inteiro e uma matriz.
    Conta quantas vezes o número aparece como elemento
    da matriz.
    int, list->int"""
    contagem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                contagem += 1
    return contagem