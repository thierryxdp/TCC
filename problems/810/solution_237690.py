def inverte(frase):
    frase = frase.replace(","," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("."," ")
    frase = frase.lower
    lista = str.split(frase)
    frase = lista.reverse()
    frase = frase.join
    return frase