def inverte(frase):
    s = frase.replace('.',' ').replace(',',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ').replace(':',' ').replace('...',' ')
    frase_invertida = s.reverse()
    return frase_invertida