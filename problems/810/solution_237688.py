def inverte(frase):
    frase = frase.replace(","," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("."," ")
    frase = frase.lower
    lista = list.split(frase)
    frase = lista.reverse()
    frase = frase.join
    return frase