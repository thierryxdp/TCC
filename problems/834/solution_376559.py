def media_matriz(matriz):
    linha=range(len(matriz))
    coluna=range(len(matriz[0]))
    soma1=0
    soma=0
    somas=0
    media=somas/(len(matriz)*len(matriz[0]))
    
    for i in linha:
        soma1+=i
        for j in coluna:
            soma2+=j
    somas= soma1+soma2
    return round(media,2)