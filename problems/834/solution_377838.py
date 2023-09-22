def media_matriz(matriz):
    somador=0
    contador=0
    for linha in matriz:
        for num in linha:
            somador=somador+num
            contador=contador+1
    return somador/contador