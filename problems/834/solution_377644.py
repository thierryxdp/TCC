def media_matriz(matriz):
    soma=0
    contador=0
    for linha in matriz:
        for elemento in linha:
            soma+=elemento
            contador+=1
    return soma/contador