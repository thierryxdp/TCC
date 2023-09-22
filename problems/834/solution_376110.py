def media_matriz(matriz):
    '''recebe e retorna a media simples de todos os elementos da matriz
    list -> float'''
    
    soma = 0
    valores = 0
    
    for coluna in matriz:
        for elemento in coluna:
            soma = soma + elemento
            valores = valores + 1
     
    return round(soma/valores,2)