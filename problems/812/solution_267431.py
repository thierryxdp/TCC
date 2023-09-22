def retira_pontuacao(frase):
    'Retorna a frase sem qualquer sinal de pontuacao..string--string'
    frase=frase.replace('!',' ').replace('?',' ').replace('...',' ').replace(',',' ').replace(';',' ').replace('.',' ').replace('-',' ')
    return frase