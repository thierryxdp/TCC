def media_matriz(matriz):
    '''Função que retorna a média de todos os números pertencentes
    a matriz
    matriz -> list
    return float'''
    
    somatorio = 0
    elementos = 0
    for i in range(len(matriz)):
        somatorio += sum(matriz[i])
        elementos += len(matriz[i])
        media = round(somatorio / elementos, 2)
    return media