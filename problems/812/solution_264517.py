def retira_pontuacao(frase):
    '''funcao que dada uma frase retorne uma frase onde todos os caracteres de pontuação sejam substituidos por espaço
    str->str'''
    return frase.replace(':',' ').replace(',',' ').replace('.',' ').replace('-',' ').replace(!,' ').replace('?',' ')