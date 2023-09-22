def media_matriz(matriz):
    """Retorna a média de todos os números dentro da matriz
       list --> float"""
    acumulador = 0
    elementos = 0
    
    for i in matriz:
        for j in i:
            acumulador += j
            elementos += len(i)
    return round(acumulador / elementos,2)