def inverte(frase):
    frase1 = frase.replace(","," ")
    frase2 = frase1.replace("!"," ")
    frase3 = frase2.replace("."," ")
    frase4 = frase3.split(" ")
    return frase4