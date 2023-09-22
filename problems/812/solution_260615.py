def retira_pontuacao(frase):
    a = str.punctuation
    if frase in a:
        b = str.replace(a, '')
        return b