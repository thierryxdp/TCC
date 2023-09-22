def uppCons(frase):
    ''' '''
    i=0
    frase_nova=[]
    while i<len(frase):
        if frase[i] in "çbcdfghjklmnpqrstvxwyz":
            frase_nova.append(frase_nova[i].upper())
        i+=1
    return frase_nova