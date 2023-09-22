def media_matriz(matriz):
    """ Função que dada uma matriz de números interos,
    retorna a média de todos os números da matriz
    Entrda: int
    Saída: float """
    soma = 0
    divisao = 0
    for x in matriz:
        soma = soma + sum(x)
        divisao  = divisao + len(x)
    return round(soma/divisao,2)