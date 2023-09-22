"""Retorna a frase invertida:
str->str"""
def conta_frases(frase):
    if not "!" and "." and "..." and "?" in frase:
        return 1
    if not "!" and "." and "..." in frase:
        return 2