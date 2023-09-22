def inverte(frase):
    frase1 = frase.lower()
    frase2 = frase1.reverse()
    frase3 = frase2.replace(","," ")
    frase4 = frase3.replace("!"," ")
    frase5 = frase4.replace("."," ")
    frase6 = frase5.replace("-"," ")
    frase7 = frase6.split(" ")
    frase8 = " ".join(frase7)
    return frase8