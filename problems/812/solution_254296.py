def retira_pontuacao(frase):
    frase.replace(frase.punctuation, '')
    return frase