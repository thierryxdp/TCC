def conta_numero(n, matriz):
    """função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer conta e retorna quantas vezes aquele número aparece na matriz"""
    soma = 0
    for x in range(len(matriz)):
        soma += list.count(matriz[x], n)
    return soma