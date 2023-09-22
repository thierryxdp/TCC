import math

def media_matriz(matriz):
    """retorna a media da matriz
    list -> float"""
    
    
    matriz_soma = []

    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            a = matriz[i][j]
            matriz_soma.append(a)
    soma = sum(matriz_soma)
    
    qtd = len(matriz_soma)
    
    resultado = round(soma/qtd,2)
    
    return resultado
    
    resultado = round(soma/qtd,2)
    
    return resultado