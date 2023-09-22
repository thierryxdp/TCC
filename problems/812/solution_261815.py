def retira_pontuacao(frase):
    '''Retira a pontuação da frase de entrada, 
       substituindo-as por espaços em branco;
       str -> str'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace(frase[-1],' ')