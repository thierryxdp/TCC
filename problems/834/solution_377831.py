def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz(com duas casas decimais de
    precisão;list->float"""
    soma=0
    denominador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            denominador=denominador+1
    media=soma/denominador
    return round(media,2)