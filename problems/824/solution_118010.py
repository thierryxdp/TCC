def uppCons(frase):
    ''' '''
    frase_nova=''
    i=0
    while i<len(frase_nova):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase_nova=frase_nova.upper()
        i+=1
    return frase_nova