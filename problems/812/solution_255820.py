import re
def retira_pontuacao(text):
    for char in ".!?,":
        text = text.replace(char, " ")
    return text