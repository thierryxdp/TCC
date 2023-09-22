def retira_pontuacao(frase):
    s = frase
    saida = s.translate(str.maketrans('', '', s.punctuation))
    return saida