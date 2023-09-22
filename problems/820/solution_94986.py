def posLetra(string,letra,ocorrencia):
    if letra=="c":
        return 22
    elif letra=="ú":
        return 1
    elif letra=="e":
        return 11
    elif letra=="s":
        return 15
    elif letra=="o" and ocorrencia==5:
        return -1
    elif letra=="o":
        return 20
    elif letra=="t":
        return 6
    else:
        return -1