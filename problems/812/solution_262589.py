import string
def retira_pontuacao(frase):
    punct = string.punctuation
    for c in punct:
    frase = frase.replace(c, "")
    return frase