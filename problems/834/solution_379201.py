def media_matriz(matriz):
    len(matriz)=x
    len(matriz[0])=y
    contador = 0
    n=0
    while n<x:
        contador = contador + sum(matriz[n])
        n = n +1
    return contador / (x*y)