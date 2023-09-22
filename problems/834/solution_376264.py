def media_matriz(matriz):
    '''função que dado uma matriz de inteiros, retorna a media de todos os numeros 
    da matriz. list -> float'''
    soma = 0
    divisor = len(matriz)*len(matriz[0])
    for n in range(len(matriz)):
        soma += sum(matriz[n])
    return round(soma / divisor,2)