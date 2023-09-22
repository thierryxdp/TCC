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
    frase = str.split(frase,' ') [::-1]
    frase = str.join(' ',frase)
    return str.lower(frase)