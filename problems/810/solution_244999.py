def inverte (frase):
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("-", " ")
    frase = frase.lower()
    separar = frase.split()
    separar.reverse()
    " ".join(separar)
    return frase