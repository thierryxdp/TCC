def inverte(frase):
    lista = str.split(frase)
    lista[::-1]
    frase = str.join(" ", lista)
    return frase