def media_matriz(matriz):
    linha=range(len(matriz))
    coluna=range(len(matriz[0]))
    soma=0
    media=soma/(len(matriz)*len(matriz[0]))
    
    for i in linha:
        soma+=i
        for j in coluna:
            soma+=i
            soma+=j
    return round(media,2)