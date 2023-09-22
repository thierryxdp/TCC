import re
def retira_pontuacao(frase):
    for caractere in "!@#$%*()<>:|/?":
        x = frase.replace(caractere, "")
    return x