from math import*
def conta_frases(frase):
    """função que calcula a quantidade de palavras
    tendo seus separadores como (. ! ? ...)
    str-> int"""
    return str.count(frase,'.')+ str.count(frase,'!')+ str.count(frase,'?')-2* str.count(frase'...')