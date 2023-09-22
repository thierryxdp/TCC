def uppCos(frase):
    indice=0
    UC=""
    while indice <= (len(frase)-1):
        if frase[indice] in "BCDFGHJKLMNPQRSTVXYWZbcdfghjklmnpqrstvxywz":
            UC= UC + frase[indice].upper()
        else:
            UC=UC +frase[indice]
        indice= indice + 1
    return UC