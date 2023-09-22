def uppCons(frase):
    ''' '''
    i=0
    frase_nova=''
    while i<len(frase_nova):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase[i]=frase[i].upper()
            frase_nova+=frase[i]
        else:
            frase[i]=frase[i]
        i+=1
    return frase_nova