def conta_numero(numero, matriz):
    """dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele numero aparece na matriz"""
    if numero in range(matriz):
        return list.count(numero, matriz)
    else:
        return 0