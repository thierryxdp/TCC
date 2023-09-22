def retira_pontuacao(frase):
    frase2=frase
    frase2= frase2.replace('.',' ')
    frase2= frase2.replace('-',' ')
    frase2= frase2.replace(',',' ')
    frase2= frase2.replace(';',' ')
    frase2= frase2.replace(':',' ')
    frase2= frase2.replace('?',' ')
    frase2= frase2.replace('!',' ')
    return frase2