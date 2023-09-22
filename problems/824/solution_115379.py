def uppCons(frase):
    '''str->str
    '''
    i=0
    
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXZbÇcdfghjklmnpqrstvwxzç':
            frase=frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase