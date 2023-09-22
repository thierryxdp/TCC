"""Retorna a frase invertida:
str->str"""
def inverte(frase):
    lista = str.split(frase)
    frase = str.join(" ", lista)
    return frase