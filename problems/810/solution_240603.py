def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('!',' ')
    frase.replace('-',' ')
    palavras[::-1]
    return ' '.join(palavras)