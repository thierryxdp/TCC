import re
def retira_pontuacao(frase):
    return "".join([char if char in ".!?," else "" for char in frase)