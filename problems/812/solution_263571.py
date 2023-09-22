def retira_pontuacao(frase):
    return frase.translate(string.maketrans("",""), string.punctuation)