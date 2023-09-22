def retira_pontuacao(frase):
    l=frase.translate(str(frase.maketrans(',')))
    return l