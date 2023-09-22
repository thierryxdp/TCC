def retira_pontuacao(frase):
    l=frase.translate(str.maketrans(','))
    return l