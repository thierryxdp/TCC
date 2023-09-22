def inverte(frase):
    frase2=frase
    frase2= frase2.replace('.',' ')
    frase2= frase2.replace('-',' ')
    frase2= frase2.replace(',',' ')
    frase2= frase2.replace(';',' ')
    frase2= frase2.replace(':',' ')
    frase2= frase2.replace('?',' ')
    frase2= frase2.replace('!',' ')
    frase2= frase2.replace('...',' ')
    str.lower(frase2)
    return frase2[::-1]