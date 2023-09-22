def retira_pontuacao(frase):
    frase.replace(str.punctuation, '')
    return frase