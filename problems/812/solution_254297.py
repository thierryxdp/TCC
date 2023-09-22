def retira_pontuacao(frase):
    import string
    pontuacao = string.punctuation
    frase.replace(pontuacao,'')
    return frase