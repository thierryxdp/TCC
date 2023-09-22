def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    lista = frase
    return  lista.replaceAll(\p{Punct})