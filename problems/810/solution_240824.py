def inverte (frase):
    frase.replace('.',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('!',' ')
    frase.replace('-',' ')
    return ' '.join(frase)