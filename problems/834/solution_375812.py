def media_matriz(matriz):
    '''função que calcula e retorna a média de todos os elementos de uma matriz de entrada com duas casas decimais; list(lists) -> float'''
    
    numerador = 0
    denominador = len(matriz[0])*len(matriz)
    
    for i in range(len(matriz)):
        numerador = numerador+sum(matriz[i]):
            
    return round(numerador/denominador,2)