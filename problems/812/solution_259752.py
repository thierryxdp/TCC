def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    sem = frase.replace('.',' '),frase.replace('!',' ')
    return sem