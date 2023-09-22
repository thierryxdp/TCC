def inverte (frase):
    palavras=frase.split( )
    palavras.reverse( )
    replace('.',' ')
    return ' '.join(palavras)