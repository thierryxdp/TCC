def inverte (frase):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    ponto =  (".", ",", "!", ":", ";", "-","?")
    frase = str.replace(ponto, " ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase.lower()