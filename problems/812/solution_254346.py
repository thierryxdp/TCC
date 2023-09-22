def retira_pontuacao(frase):
    import string
    novafrase = frase.translate(str.maketrans('', '', string.punctuation))
    return novafrase