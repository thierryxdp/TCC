def retira_pontuacao(frase):
    nova_frase= frase.translate(str.maketrans('', '', string.punctuation))
    return nova_frase