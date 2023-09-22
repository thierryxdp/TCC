def inverte(frase):
    frase = frase.replace("."," ")
    lista = str.split(frase)
    lista.reverse()
    return frase