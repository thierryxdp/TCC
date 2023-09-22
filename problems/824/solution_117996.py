def uppCons(frase):
    ''' '''
    i=0
    frase_nova=''
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase_nova=frase_nova.upper()+frase[i:]
        i+=1
    return frase_nova