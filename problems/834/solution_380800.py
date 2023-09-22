def media_matriz(matriz):


    total_elementos = len(matriz)*len(matriz[0])
    soma_numeros = 0
    for l in matriz:
        soma_numeros+=sum(l)
    media = (soma_numeros)/(total_elementos)
    return round(media,2)