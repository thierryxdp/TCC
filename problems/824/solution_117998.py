def uppCons(frase):
    ''' '''
    i=0
    frase_nova=[]
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase_nova.append(frase_nova.upper())
        i+=1
    return frase_nova