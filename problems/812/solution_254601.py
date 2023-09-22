import string

def retira_pontuacao(frases):
    return frases.translate(string.maketrans("",""), string.punctuation)