def retira_pontuacao(frase):
    frase = str(frase).replace('!',' ')
    frase = str(frase).replace('-',' ')
    frase = str(frase).replace('?',' ')
    frase = str(frase).replace('.',' ')
    frase = str(frase).replace(',',' ')
    frase = str(frase).replace(':',' ')
    frase = str(frase).replace(';',' ')
    return frase