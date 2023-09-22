def media_matriz(matriz):
    """dado como paramêtro uma matriz de numeros inteiros e
    não vazia, a função retorna a média de todos os numeros
    da matriz com no maximo duas casas decimais de precisão;
    list -> int"""
    total = 0
    for i in range(len(matriz)):
        for j in i:
            total = total + j
    return total