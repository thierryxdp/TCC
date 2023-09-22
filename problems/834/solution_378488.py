def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia, retorna
    a média de todos os números da matriz (com duas casas
    decimais de precisão).
    list -> float'''
    num_linhas=len(matriz)
    num_colunas=len(matriz[0])
    numerador=0
    denominador=num_colunas*num_linhas
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador = numerador + sum(matriz[j])
    media=numerador/denominador
    media_arredondada=round(media,2)
    return media_arredondada