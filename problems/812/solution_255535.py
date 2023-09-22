def retira_pontuacao(frase):
    s = frase
    saida = s.translate(s.maketrans('!', ''))
    return saida