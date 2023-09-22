def conta_numero(numero,matriz):
    """Dado um número inteiro e uma matriz de números inteiros de tamanho
    qualquer, a função retorna quantas vezes aquele número aparece na matriz;
    int, list(list(int)) -> int"""
    qtd_numero = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                qtd_numero = qtd_numero + 1
    return qtd_numero