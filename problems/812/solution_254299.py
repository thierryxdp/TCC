def retira_pontuacao(frase):
    import string
    pontuacao = string.punctuation
    str.split(pontuacao)
    frase.replace(pontuacao,'')
    return frase