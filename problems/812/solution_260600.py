def retira_pontuacao(frase):
    '''
    funcao retira a pontuacao da string
    '''
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    return frase