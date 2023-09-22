def inverte (frase):
    frase = str.split(frase)
    list.reverse(frase)
    return str.lower(retira_pontuacao(', '.join(frase)))