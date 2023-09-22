def uppCons(frase):
    """ oi """
    i=0
    frase2=''
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frase2=frase2+frase[i].upper()
            i=i+1
        else:
            frase2=frase2+frase[i]
            i=i+1
    return frase2