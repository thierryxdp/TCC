def media_matriz(matriz):
    '''Dada uma matriz inteira não vazia, retorna a média de todos os números da matriz
    matriz->int'''
    
    acumulador=0
    denominador=len(matriz)*len(matriz[0])
    
    for a in range(len(matriz)):
        for b in matriz[a]:
            acumulador+=b
    final=acumulador/denominador
    return final