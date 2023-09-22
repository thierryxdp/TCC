def media_matriz(matriz):
    """Retorna a média de todos os números dentro da matriz
       list --> float"""
    acumulador = 0
    elementos = 0
    
    for i in matriz:
        elementos += len(i)
        for j in i:
            acumulador += j
    return round((acumulador / elementos),2)