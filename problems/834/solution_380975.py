def media_matriz(matriz):
    i=0
    soma=0
    qtd=0
    while i<len(matriz):
        j=0
        while j < len(matriz[i]):
            soma +=1 matriz[i][j]
            qtd +=1
            j +=1
        i +=1
    media=soma/qtd
    return round(media,2)