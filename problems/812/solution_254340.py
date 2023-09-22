def retira_pontuacao(frase):
    import string
    pontuacao = string.punctuation
    for x in pontuacao:
        frase = frase.replace(x,' ')
        return frase