def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros, conta e retorna
    quantas vezes aquele número aparece na matriz"""
    contador = 0
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if matriz[linha][coluna] == numero:
                contador += 1

    return contador