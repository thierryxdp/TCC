def inverte (frase):
    frase.replace('.',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('!',' ')
    frase.replace('-',' ')
    palavras=frase.reverse( )
    return ' '.join(palavras)