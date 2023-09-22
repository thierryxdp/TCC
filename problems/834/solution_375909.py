def media_matriz():
    contadorsoma=0
    contadoritens=0
    for x in matriz:
        for y in x:
            contadorsoma+=y
            contadoritens+=1
    return contadorsoma/contadoritens