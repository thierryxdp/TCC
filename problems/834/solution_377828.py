def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz(com duas casas decimais de
    precisão;list->float"""
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
    return round(soma,2)