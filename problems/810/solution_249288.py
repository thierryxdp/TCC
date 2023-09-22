def inverte(frase):
    s = frase.replace('.',' ').replace(',',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ').replace(':',' ').replace('...',' ')
    s[::-1]
    return s