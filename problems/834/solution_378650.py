def media_matriz(matriz):
    """dada uma matriz ela retorna a média de todos os
    números da matriz"""
    lin = len(matriz)
    col = len(matriz[0])
    i = 0
    soma = 0
    while i < lin:
        soma = soma + sum(matriz[i])
        i = i + 1
    return round(soma/(lin*col),2)