def inverte(frase):
    '''teste'''
    frase2=str.lower(frase)
    frase3=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase2,'!',' '),'?',' '),'-',' '),':',' '),';',' '),'.',' '),',',' ')
    lista=frase3.split()

    return str.join(' ',lista[-1::-1])