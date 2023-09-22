def conta_numero(numero, matriz):
    """Função que dado um número inteiro e uma matriz de inteiros conta e retorna quantas vezes aquele número aparece,
    int, list --> int"""
    cont = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == numero:
                cont += 1
    return cont