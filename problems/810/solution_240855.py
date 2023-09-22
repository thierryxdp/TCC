def retira_pontuacao (frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    return frase
def inverte (frase):
    frase.reverse( )
    return ' '.join(frase)