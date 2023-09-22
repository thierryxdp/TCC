def inverte(frase):
    '''Rerorna a frase invertida
    str -> str'''
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase