def inverte (frase):
    palavras=frase.split( ) and frase.replace('.',' ')
    palavras.reverse( )
    return ' '.join(palavras)