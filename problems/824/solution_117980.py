def uppCons(frase):
    ''' '''
    i=0
    frase_nova=''
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase[i]=frase[i].upper+frase[i:]
            i+=1
    return frase_nova