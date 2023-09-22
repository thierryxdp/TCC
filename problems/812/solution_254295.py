def retira_pontuacao(frase):
    pontuação = frase.punctuation
    frase.replace(pontuação, '')
    return frase