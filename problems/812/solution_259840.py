def retira_pontuacao(frase):

    frase2=frase.replace('-',' ')    
    frase3=frase2.replace(',',' ')
    frase4=frase3.replace(':',' ')
    frase5=frase4.replace(';',' ')
    frase6=frase5.replace('.',' ')
    frase7=frase6.replace('!',' ')
    return frase7