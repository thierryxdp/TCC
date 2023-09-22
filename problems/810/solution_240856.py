def inverte (frase):
    frase=frase.split( )
    frase=frase.replace('.',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace(',',' ')
    frase.reverse( )
    return ' '.join(frase)