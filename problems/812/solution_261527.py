def retira_pontuacao(frase):
    """função que retira as pontuações da frase
    str -> str"""
    return ((str.replace(frase,'-',' ')) and (str.replace(frase,',',' ')) and (str.replace(frase,'.',' ')))