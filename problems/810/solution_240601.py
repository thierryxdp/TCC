def inverte (frase):
    palavras=frase.split( )
    palavras=frase.replace('.',' ')
    palavras=frase.replace('?',' ')
    palavras=frase.replace(',',' ')
    palavras=frase.replace('!',' ')
    palavras=frase.replace('-',' ')
    palavras[-1:]
    return ' '.join(palavras)