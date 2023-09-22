def retira_pontuacao(frase):
    l=frase.translate(frase.maketrans(','))
    return l