def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    del.especiais = "!?.,;:-"
    return str.replace(frase, 'especiais', ' ')