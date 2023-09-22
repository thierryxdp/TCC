def media_matriz(matriz):
    x = len(matriz) 
    y = len(matriz[0])
    contador = 0
    n=0
    while n<x:
        contador = contador + sum(matriz[n])
        n = n +1
    return round(contador / (x*y),2)