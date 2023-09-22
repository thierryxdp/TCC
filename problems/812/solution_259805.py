def retira_pontuacao(frase):
    '''Dada uma frase, retorna todos os caracteres de pontuação substituídos por espaços; string -> string'''
    return frase.replace('...',' ').replace('.',' ').replace('?',' ').replace('!',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ')