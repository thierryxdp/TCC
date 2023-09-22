def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;
    int-->flot'''
    soma = 0
    for l in range(len(matriz)):
        soma = soma + sum(matriz[l])
    media = soma / (len(matriz)* len(matriz[0]))
    return round(media,2)