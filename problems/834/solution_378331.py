def media_matriz(matriz):
    """Retorna a média dos números de uma dada matriz não-vazia de números inteiros.
    Entrada: list(list)
    Saída: float
    """
    qtd = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        	soma += matriz[i][j]
            qtd += 1
    return soma/qtd