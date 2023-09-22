def inverte(frase):
    """Tem como objetivo inverter a ordem de uma frase.
    str > str"""
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase