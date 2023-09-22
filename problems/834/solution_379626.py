def media_matriz(matriz):
    """Função que, dada uma matriz de inteiros não vazia,
    retorna a média de todos os números da matriz.
    matriz->float"""
    soma=0
    total=len(matriz)*len(matriz[0])
    for i in matriz:
        for j in i:
            soma=soma+j
    return round(soma/total,2)