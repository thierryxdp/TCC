def media_matriz(matriz):
    '''
    Retorna a média dos números de uma matriz;
    list -> float
    '''
    
    acumulador = 0
    for line in matriz:
        for valor in line:
            acumulador += valor
    return round(acumulador / (len(matriz) * len(matriz[0])), 2)