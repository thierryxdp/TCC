def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;
    int-->flot'''
    soma = 0
    for R in range(len(matriz)):
        soma = soma + sum(matriz[R])
        media = soma / (len(matriz)* len(matriz[0]))
        return round(media,2)