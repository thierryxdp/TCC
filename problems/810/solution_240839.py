def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace(',',' ')
    palavras.reverse( )
    str.lower(palavras.reverse( ))
    return ' '.join(palavras)