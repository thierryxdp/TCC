def inverte(frase):
    frase1 = frase.lower()
    frase2 = frase1.split(" ")
    frase3 = frase2.reverse()
    frase4 = " ".join(frase2)
    return frase4