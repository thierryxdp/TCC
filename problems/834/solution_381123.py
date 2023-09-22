def media_matriz(matriz):
    soma = 0 
    divisor = 0
    for lista in matriz:
        for numero in lista:
            soma += numero
            divisor += 1
    return round(soma/divisor,2)