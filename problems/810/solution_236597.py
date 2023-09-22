def inverte(frase):
    frase1 = frase.lower()
    frase2 = frase1.replace("-"," ")
    frase3 = frase2.split(" ")
    frase4 = frase3.reverse()
    frase5 = " ".join(frase3)
    frase6 = frase5.replace(".","")
    frase7 = frase6.replace("!","")
    frase8 = frase7.replace("?","")
    frase9 = frase8.replace(",","")
    return frase9