def inverte(frase):
    '''..'''
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('^',' ')
    frase = frase.replace('~',' ')
    frase = frase.replace('´',' ')
    frase = frase.replace('`',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('/',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('_',' ')
    frase = frase.split(frase,' ') [-1::-1]
    frase = frase.join(' ',frase)
    return str.lower(frase)