def inverte (frase):
    palavras=frase.split( )
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    palavras.reverse( )
    return ' '.join(palavras)