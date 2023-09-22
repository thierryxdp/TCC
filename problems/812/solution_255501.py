def retira_pontuacao(frase):
    s = frase
    saida = s.translate(str.maketrans('', '', string.punctuation))
    return saida