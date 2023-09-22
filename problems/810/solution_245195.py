def invert(frase):
    """ Função que dada uma frase, ela é retornada sem çetras maiusculas,
    e sem pontuação. str -> str"""
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", frase_invertida)
    return frase