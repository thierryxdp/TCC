def media_matriz(matriz):
    """faz a média aritmética de tosos os números em uma matriz. LIST->FLOAT"""
    somador=0
    contador=0
    for linha in matriz:
        for num in linha:
            somador=somador+num
            contador=contador+1
    return round(somador/contador,2)