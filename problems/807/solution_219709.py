"""Retorna a frase invertida:
str->str"""
def conta_frases(frase):
    if "!" and "." and "..." and "?" in frase:
        return 1
    if "!" and "." and "..." in frase:
        return 2