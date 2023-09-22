"""Recebe uma string e retorna a mesma com a substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    frase2 = ""
    frase2 =+ frase.replace(".", " ")
    frase2 =+ frase.replace("...", " ")
    frase2 =+ frase.replace(",", " ")
    frase2 =+ frase.replace(";", " ")
    frase2 =+ frase.replace("!", " ")
    frase2 =+ frase.replace("?", " ")
    frase2 =+ frase.replace(":", " ")
    frase2 =+ frase.replace("—", " ")
    return frase2