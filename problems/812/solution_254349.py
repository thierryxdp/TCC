def retira_pontuacao(frase):
    import string
    pontuacao = string.punctuation
    pontuacao = str.split(pontuacao)
    for x in pontuacao:
        frase = frase.replace(x,' ')
        return frase