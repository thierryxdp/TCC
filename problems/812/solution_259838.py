def retira_pontuacao(frase):

    frase2=frase.replace('-',' ')    
    frase2=frase.replace(',',' ')
    frase2=frase.replace(':',' ')
    frase2=frase.replace(';',' ')
    frase2=frase.replace('.',' ')
    frase2=frase.replace('!',' ')
    return frase2