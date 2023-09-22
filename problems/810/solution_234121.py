def inverte(frase):
    '''Retorna uma frase com as palavras na ordem inversa à frase dada'''
    '''str -> str'''
    return str.lower(str.join(' ',(str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),'...',' '),'-',' '),',',' '),';',' '),':',' '))[::-1]))