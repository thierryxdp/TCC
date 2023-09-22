def inverte (frase):
    palavras=frase.split( )
    palavras.reverse( )
    frase.replace('.',',')
    return ' '.join(palavras)