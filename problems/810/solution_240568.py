"""Retorna a frase invertida:
str->str"""
def inversa(frase):
    lista = str.split(frase)
    frase = str.join(" ", lista)
    return frase