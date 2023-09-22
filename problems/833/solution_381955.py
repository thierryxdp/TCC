def conta_numero(numero, matriz):
    """Função que recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retornando quantas vezes aquele numero aparece na matriz
    entrada: int, list(list)
    retorno: int"""
    vezes= 0
    for i in range(len(matriz)):
        vezes += list.count(matriz[i],numero)
    return vezes