def media_matriz(matriz):
    contadorsoma=0
    contadoritens=0
    for x in matriz:
        for y in x:
            contadorsoma+=y
            contadoritens+=1
    return round(contadorsoma/contadoritens,2)