def inverte (frase,separa):
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("-", " ")
    frase = frase.lower()
    separa = frase.split()
    separa = separa.reverse()
    return frase