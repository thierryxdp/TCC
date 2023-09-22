def media_matriz(media):
    contadorsoma=0
    contadoritens=0
    for x in matriz:
        for y in x:
            contadorsoma+=y
            contadoritens+=1
    return contadorsoma/contadoritens