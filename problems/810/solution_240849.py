def inverte (frase):
    frase=frase.split( )
    frase=frase.replace('.',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace(',',' ')
    frase.reverse( )
    frase.lower()
    return ' '.join(frase)