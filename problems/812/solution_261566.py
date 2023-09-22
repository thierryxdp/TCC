def retira_pontuacao(frase):
    """função que retira todas as pontuações da frase
    str -> str"""
    frase1 = str.replace(frase,',',' ')
    frase2 = str.replace(frase1,'-',' ')
    return frase2