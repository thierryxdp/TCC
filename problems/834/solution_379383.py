def media_matriz(matriz):
    """função que dada uma matriz  de inteiros não vazia,retorna a media de todos os numeros da matriz; matriz--.matriz"""
    soma = 0
    for l in range(len(matriz)):
        soma = soma + sum(matriz[l])
    media = soma / (len(matriz)*len(matriz[0]))
    return round(media,2)