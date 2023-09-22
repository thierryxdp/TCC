def inverte(frase):
    '''inverte a ordem das palavras na frase'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,';',' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    list.reverse(frase)
    frase = str.join(' ',frase)
    return frase