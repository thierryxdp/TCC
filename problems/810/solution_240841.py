def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace(',',' ')
    str.lower(palavras.reverse( ))
    return ' '.join(palavras)