def inverte (frase):
    palavras=frase.split( )
    palavras=frase.replace('.',' ')
    palavras=frase.replace('?',' ')
    palavras=frase.replace(',',' ')
    palavras=frase.replace('!',' ')
    palavras=frase.replace('-',' ')
    palavras.reverse( )
    return ' '.join(palavras)