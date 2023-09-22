def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    remove.especiais = "!?.,;:-"
    return str.replace(frase, 'especiais', ' ')