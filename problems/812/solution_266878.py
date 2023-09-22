def retira_pontuacao(frase):
    frase=str.punctuation(frase)
    return frase.replace(frase,"")