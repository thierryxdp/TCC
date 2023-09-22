def conta_numero(numero, matriz):
    """Função que recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retornando quantas vezes aquele numero aparece na matriz
    entrada: int, list(list)
    retorno: int"""
    vezes= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == numero:
                vezes += 1
    return vezes