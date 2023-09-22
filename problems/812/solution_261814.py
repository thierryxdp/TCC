def retira_pontuacao(frase):
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace(frase[-1],' ')