def retira_pontuacao(frase):
    '''faz ae'''
    return frase.replace(',',' ').replace('-',' ').replace('.',' ').replace('!',' ').replace('?',' ').replace(';',' ').replace(':',' ')