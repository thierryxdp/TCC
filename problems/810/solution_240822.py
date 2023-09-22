def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('!',' ')
    frase.replace('-',' ')
    palavras=frase.reverse( )
    return ' '.join(palavras)