def media_matriz(matriz):
    indice = 0
    contador = 0
    soma = 0
    for i in matriz:
        for j in matriz[indice]:
            soma = soma + j 
            contador =+ 1
            indice += 1
    media = soma/contador
    return round(media,2)