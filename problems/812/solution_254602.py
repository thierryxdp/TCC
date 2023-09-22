import string

def retira_pontuacao(frases):
    return frases.translate(frases.maketrans("",""), frases.punctuation)