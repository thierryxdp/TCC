def uppCons(frase):
    ''' '''
    i=0
    frase_nova=''
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase[i]=frase[i].upper()
            frase_nova+=frase[i]
        else:
            frase[i]=frase[i]
        i+=1
    return frase