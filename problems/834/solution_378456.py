# Função que dada uma matriz de inteiros nao vazia, retorne a media de todos os numeros da matriz
# Variavel matriz
#param matriz: list -> list return: float -> float
"""Dada uma matriz, calcula a média de todos os valores dessa matriz.:param matriz: list -> list :return: float -> float"""
soma = 0
tamanho = 0
media = 0
if matriz != []:
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            tamanho += 1
            soma += matriz[lin][col]
            media = soma / tamanho
    return round(media, 2)