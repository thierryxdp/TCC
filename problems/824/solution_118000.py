def uppCons(frase):
    ''' '''
    frase=list(frase)
    i=0
    frase_nova=[]
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase_nova.append(frase.upper())
        i+=1
    return frase_nova