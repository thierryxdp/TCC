def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    sem1 = frase.replace('.',' ')
    sem2 = frase.replace('!',' ')
    sem3 = frase.replace('?',' ')
    sem4 = frase.replace('-',' ')
    return sem4