def uppCons(frase):
    ''' recebe uma frase e deixa todas as suas consoante maiusculas
    str->str'''
    list(frase)
    i=0
    c="bcdfghjklmnpqrstvywzBCDFGHJKLMNPQRSTVYWZ"
    while i<len(frase):
        if c in frase[i]:
            frase[i].upper()
        i=i+1
    return ' '.join(frase)