def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    return str.replace(frase, "- : ; ;", " ")