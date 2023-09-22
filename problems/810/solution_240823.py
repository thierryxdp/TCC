def inverte (frase):
    palavras=frase.split( )
    frase.replace('.',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('!',' ')
    frase.replace('-',' ')
    return ' '.join(palavras)