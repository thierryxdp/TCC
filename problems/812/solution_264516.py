def retira_pontuacao(frase):
    '''funcao que dada uma frase retorne uma frase onde todos os caracteres de pontuação sejam substituidos por espaço
    str->str'''
    str.join(frase," ")
    return frase.replace(':',' ').replace(',',' ').replace('.',' ').replace('-',' ').replace(!,' ').replace('?',' ')