def media_matriz(matriz):
    soma = 0
    i = 0
    quantidade = 0

    if len(matriz)!=0:
        while i< len(matriz):
            soma+= sum(matriz[1])
            quantidade += len(matriz[1])
            i +=1
    media =soma/quantidade
    return round (media,2)