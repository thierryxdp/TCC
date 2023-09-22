def uppCons(frase):
    ''' recebe uma frase e deixa todas as suas consoante maiusculas
    str->str'''
    list(frase)
    i=0
    frase1=( )
    c="bcdfghjklmnpqrstvywzBCDFGHJKLMNPQRSTVYWZ"
    while i<len(frase):
        if frase[i] in c:
            frase1= frase1 + frase[i].upper()
        i=i(frase)
    return frase1