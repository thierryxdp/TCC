def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    replace(',',' ')
    palavras.reverse( )
    return ' '.join(palavras)