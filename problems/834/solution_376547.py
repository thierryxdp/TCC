def media_matriz(matriz):
    """
    Função que recebe uma matriz de números inteiros
    e retorna a média de todos os
    elementos dessa matriz.
    
    list --> float
    """
    soma=0
    for linha in matriz:
        for elemento in linha:
            soma+=elemento
    media=round(soma/(len(matriz)*len(matriz[0])),2)
    return media