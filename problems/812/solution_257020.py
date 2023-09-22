def retira_pontuacao(frase):
    x= frase.replace('...',' ').replace('-',' ').replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace('.',' ').replace('/',' ').replace(':',' ').replace(';',' ')
    return x