def media_matriz(matriz):
    cont1=0
    soma=0
    quantidade=0
    while cont1<len(matriz):
        cont2=0
        while j<len(matriz[cont1]):
            soma+=matriz[cont1][cont2]
            quantidade+=1
            cont2+=1
        cont1+=1
    media=soma/quantidade
    return round(media,2)