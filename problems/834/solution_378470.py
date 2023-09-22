def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia, retorna
    a média de todos os números da matriz (com duas casas
    decimais de precisão).
    list -> float'''
    num_linhas=len(matriz)
    num_colunas=len(matriz[0])
    indice=range(num_colunas)
    numerador=0
    denominador=num_colunas*num_linhas
    media=numerador/denominador
    for i in matriz:
        for j in matriz[0]:
            numerador = numerador + j
    return media