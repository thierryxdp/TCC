def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    especiais = "!?.,;:-"
    return str.replace(frase, "especiais", " ")