def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    list -> int"""
    repetiu = 0
    for indice in range(0, len(matriz)):
        repetiu += 1
        if matriz[indice] == numero:
    return repetiu