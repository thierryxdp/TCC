"""Retorna a frase sem pontuação:
str->str"""
def retira_pontuacao(frase):
    frase = str.split(frase, "! and : and . and ? and , and -")
    frase = str.join(" ", frase)
    return frase