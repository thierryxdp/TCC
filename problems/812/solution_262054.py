def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna todos caracteres de pontuacao substituidos por espaco
    str-> str
    '''
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('...',' ')
    frase=frase.replace('.',' ')
    return frase