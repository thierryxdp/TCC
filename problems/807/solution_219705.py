"""Retorna a frase invertida:
str->str"""
def conta_frases(frase):
    if "!" and "." and "..." and "?" in frase:
        return 4
    if "!" and "." and "..." in frase:
        return 3