def inverte (frase):
    palavras=frase.split( )
    palavras.reverse( )
    frase.replace('.',',')
    frase.reverse()
    return ' '.join(palavras)