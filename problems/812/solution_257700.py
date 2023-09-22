def retira_pontuacao(frase):
    """" retira a pontução das frases;str->str"""
    frases= str.split(frase)
    return frases - frases[-]