def retira_pontuação(frase):
    frase = frase.replace('.',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('?',' ')
    return frase