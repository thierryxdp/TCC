def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    s = frase
    new = s.replace('.',' ')
    return new