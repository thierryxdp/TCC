def substituir(frase):
    frase = str.split(frase, "-")
    frase = str.join("#", frase)
    return frase