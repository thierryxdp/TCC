import math

def media_matriz(matriz):
    """retorna a media da matriz
    list -> float"""
    
    
    matriz_soma = []
    
    for i in range(len(matriz))-1:
        for j in range(len(matriz))-1:
            a = matriz[i-1][j-1]
            matriz_soma.append(a)
    soma = sum(matriz_soma)
    
    qtd = len(matriz_soma)
    
    resultado = round(soma/qtd,2)
    
    return resultado