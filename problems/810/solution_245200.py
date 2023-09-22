def inverte(frase):
    """ Função que dada uma frase, ela é retornada sem çetras maiusculas,
    e sem pontuação. str -> str"""
    lista = str.split(frase)
    lista.reverse()
    lista.lower()
    frase = str.join(" ", lista)
    return frase