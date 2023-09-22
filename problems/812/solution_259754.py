def retira_pontuacao(frase):
    '''retira todas as pontuações da frase'''
    sem1 = frase.replace('.',' ')
    sem2 = sem1.replace('!',' ')
    sem3 = sem2.replace('?',' ')
    sem4 = sem3.replace('-',' ')
    return sem4