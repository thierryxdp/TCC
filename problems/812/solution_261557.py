def retira_pontuacao(frase):
    """função que retira todas as pontuações da frase
    str -> str"""
    return str.replace(frase,',',' ')