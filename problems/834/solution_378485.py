def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia, retorna
    a média de todos os números da matriz (com duas casas
    decimais de precisão).
    list -> float'''
    num_linhas=len(matriz)
    num_colunas=len(matriz[0])
    numerador=0
    denominador=num_colunas*num_linhas
    media=numerador/denominador
    media_arredondada=round(media,2)
    for i in range(len(matriz)):
        for j in range(len(matriz[0]))
            numerador = numerador + sum(matriz[j])
    return media_arredondada