def media_matriz(matriz):
    """..."""
    acumulador = 0
    numero = len(matriz) * len(matriz[0])
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            acumulador = acumulador + matriz[i][j]
            
    return round(acumulador/numero:2)