def uppCons(frase):
    ''' recebe uma frase e deixa todas as suas consoante maiusculas
    str->str'''
    list(frase)
    i=0
    c="bcdfghjklmnpqrstvywzçBCDFGHJKLMNPQRSTVYWZÇ"
    while i<len(frase):
        if frase[i] in c:
            frase = frase.replace(frase[i],frase[i].upper())
        i= i + 1
    return frase