import re
def retira_pontuacao(frase):
    for char in ".!?,-":
        frase = frase.replace(char, " ")
    return frase