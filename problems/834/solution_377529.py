def media_matriz(matriz):
    soma = 0
    cont = 0
    for i in range(len(matriz)):
        if len(matriz) != 0:
            soma = soma + sum(matriz[i])
            cont = cont + len(matriz[i])
            media = soma/cont
    return round(media,2)