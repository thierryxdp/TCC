def retira_pontuacao(frase):
    frase1=frase.replace( '?' ,' ')
    frase2=frase1.replace('!',' ')
    frase3=frase2.replace('.',' ')
    frase3=frase2.replace(';',' ')
    frase4=frase3.replace(',',' ')
    frase5=frase4.replace(':',' ')
    return frase5