def retira_pontuacao(frase):
    frassemponto = frase.replace('!',' ').replace('?',' ').replace('...',' ').replace('-',' ').replace(';',' ').replace('.',' ').replace(':',' ').replace(',',' ')
    return frassemponto