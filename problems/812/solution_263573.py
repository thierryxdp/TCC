def retira_pontuacao(frase):
    import string
    return frase.translate(string.maketrans("",""), string.punctuation)