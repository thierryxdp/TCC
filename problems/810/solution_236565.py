def inverte(frase):
    frase1 = frase.replace(","," ")
    frase2 = frase1.replace("!"," ")
    frase3 = frase2.replace("."," ")
    frase4 = frase3.split(" ")
    frase5 = frase4.reverse()
    frase6 = frase.lower()
    return " ".join(frase4)