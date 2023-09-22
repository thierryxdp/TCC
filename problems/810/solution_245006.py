def inverte (frase):
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("-", " ")
    frase = frase.lower()
    separar = frase.split()
    separar = separar.reverse()
    return frase