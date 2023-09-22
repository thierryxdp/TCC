def inverte(frase):
    '''Rerorna a frase invertida
    str -> str'''
    frase=frase.replace(","," ")
    frase=frase.replace("."," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase=lower(frase)
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase