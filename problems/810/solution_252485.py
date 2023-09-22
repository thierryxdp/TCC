def inverte(frase):
    frase = str.replace("."," ")
    lista = str.split(frase)
    lista.reverse()
    return frase