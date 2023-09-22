def media_matriz(matriz):

    soma=0
    contador=0
    for linha in matriz:
        for elem in linha:
            soma+=elem
            contador+=1

    media=soma/contador

    return round(media, 2)