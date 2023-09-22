import string
def retira_pontuacao(frase):
    ''''''
    punct=string.punctuation
    return str.strip(frase,punct)