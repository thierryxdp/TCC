def media_matriz(matriz):
    soma=0
    cont=0
    for x in matriz:
        for y in x:
            soma=soma+y
            cont=cont+1
    media=soma/cont
    return round(media,2)