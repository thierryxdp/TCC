def retira_pontuacao(frase):
    """função que retira todas as pontuações da frase
    str -> str"""
    frase1 = str.replace(frase,[',','-',';',':','!','.','...','?'],' ')
    return frase1