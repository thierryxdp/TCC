def inverte(frase):
    '''teste'''
    frase2=str.lower(frase)
    frase3=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase2,'!',' '),'?',' '),'-',' '),':',' '),';',' '),'.',' '),',',' ')
    frase4=frase3.split()

    return str.join(' ',frase4[-1::-1])