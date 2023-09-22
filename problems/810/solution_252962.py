def ponto (x):
    f = x
    f = str.replace(f,',',' ')
    f = str.replace(f,'.',' ')
    f = str.replace(f,'!',' ')
    f = str.replace(f,'?',' ')
    f = str.replace(f,'-',' ')
    f = str.replace(f,';',' ')
    return f


def inverte(frase):
    '''inverte a frase'''
    i = frase
    i = ponto(i)
    i = str.lower(i)
    i = str.split(i)
    i = i[::-1]
    i = str.join(' ',i)
    return i