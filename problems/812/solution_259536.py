"""Retorna a frase sem pontuação:
str->str"""
def retira_pontuacao(frase):
    frase = str.split(frase, "!" or ":" or "." or "?" or "," or "-")
    frase = str.join(" ", frase)
    return frase