"""Retorna a quantidade de frases de uma string.
String -> int"""
def conta_frases(frase):
    return (str.count(frase, ".") - (2*str.count(frase, "...")) + str.count(frase, "!") + str.count(frase, "?"))