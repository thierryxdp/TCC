def uppCons(frase):
    ''' recebe uma frase e deixa todas as suas consoante maiusculas
    str->str'''
    i=0
    c="bcdfghjklmnpqrstvywzBCDFGHJKLMNPQRSTVYWZ"
    while i<len(frase):
        if frase[i] c:
            frase[i].uppper()
        i=i+1
    return ' '.join(frase)