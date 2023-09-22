def inverte(frase):
    '''Rerorna a frase invertida
    str -> str'''
    frase=frase.replace(","," ")
    frase=frase.replace("."," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase