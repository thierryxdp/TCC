def retira_pontuacao(frase):
    ''' função que remove a pontuação das frases'''
    frase=frase.replace(',',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    return frase