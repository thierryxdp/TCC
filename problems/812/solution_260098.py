def retira_pontuação(frase):
    "Dada uma  frase, retorna a frase onde todos  os caracteres foram substituidos por espaco. str-->str"
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('-',' ')
    return frase