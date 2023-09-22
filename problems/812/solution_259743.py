def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    list = frase
    return  list.replaceAll(\p{Punct},".")