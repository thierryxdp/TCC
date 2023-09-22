import math

def media_matriz(matriz):
    """retorna a media da matriz
    list -> float"""
    
    
    matriz_soma = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            a = lenmatriz[i][j]
            matriz_soma.append(a)
    soma = sum(matriz_soma)
    
    qtd = matriz_soma.count
    
    
    return round(soma/qtd,2)