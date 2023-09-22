def inverte(frase):
    '''Retorna a frase dada de maneira invertida, sem pontuação e em minúsculo'''
    '''str -> str'''
    ponto=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),'...',' '),'-',' '),',',' '),';',' '),':',' ')
    return str.lower(str.join(' ',(str.split(ponto)[::-1])))