def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço; string -> string'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace('.',' ').replace(';',' ').replace('?',' ').replace('!',' ')