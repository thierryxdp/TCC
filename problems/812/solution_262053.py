def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna todos caracteres de pontuacao substituidos por espaco
    str-> str
    '''
    frase.replace('-',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('?',' ')
    frase.replace('!',' ')
    frase.replace('...',' ')
    frase.replace('.',' ')
    return frase