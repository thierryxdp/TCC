def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace(',',' ')
    palavras.reverse( )
    return ' '.join(palavras)