def media_matriz(matriz):
    contador=0
    soma=0
    for i in range(len(matriz)):
        if len(matriz)==0:
            soma=soma+sum(matriz[i])
            contador=contador+len(matriz[i])
            media=soma/contador
    return round(media,2)