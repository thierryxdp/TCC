def media_matriz(matriz):
    """Função que dada uma matriz de inteiros, retorna a média de todos os números da matriz"""
    """list--->float"""
    soma=0
    quantidade=len(matriz)*len(matriz[0])
    for l in range(len(matriz)):
        soma+=sum(matriz[l])
    media=soma/quantidade
    return round(media,2)