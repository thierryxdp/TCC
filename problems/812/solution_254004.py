"""Recebe uma string e retorna a mesma com a substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    frase.replace(".", " ")
    frase.replace("...", " ")
    frase.replace(",", " ")
    frase.replace(";", " ")
    frase.replace("!", " ")
    frase.replace("?", " ")
    frase.replace(":", " ")
    frase.replace("—", " ")
    return frase