def inverte(frase):
    frase1 = frase.lower()
    frase2 = frase1.split(" ")
    frase3 = frase2.reverse()
    frase4 = " ".join(frase2)
    frase5 = frase4.replace(".","")
    frase6 = frase5.replace("!","")
    frase7 = frase6.replace("?","")
    frase8 = frase7.replace(",","")
    return frase8