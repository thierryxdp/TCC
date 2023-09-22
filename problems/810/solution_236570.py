def inverte(frase):
    frase1 = frase.replace(","," ")
    frase2 = frase1.replace("!"," ")
    frase3 = frase2.replace("."," ")
    frase4 = frase3.replace("-"," ")
    frase5 = frase4.split(" ")
    frase6 = frase5.reverse()
    frase7 = frase6.lower()
    return " ".join(frase7)