def uppCons(frase):
    '''Dada uma frase, retorna a mesma frase com as consoantes maiusculas
    str->str'''
    i=0
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç':
            frase=str.replace(frase,(frase[i]),(str.upper(frase[i])))
        i=i+1
    return frase