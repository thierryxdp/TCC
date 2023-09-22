def inverte (frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    palavras=frase.reverse( )
    return ' '.join(palavras)