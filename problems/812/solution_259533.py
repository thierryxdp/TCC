"""Retorna a frase sem pontuação:
str->str"""
def retira_pontuacao(frase):
    frase = str.split(frase, "!")
    frase = str.join(" ", frase)
    return frase