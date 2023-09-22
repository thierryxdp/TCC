def inverte(frase):
    '''Retorna a frase digitada pelo usuário invertida.
    str -> str'''
    frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),';',' '),':',' '),',',''),'-',' '),'!',' '),'?',' ')
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',frase)
    return str.lower(frase)