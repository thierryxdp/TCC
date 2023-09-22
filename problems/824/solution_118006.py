def uppCons(frase):
    ''' '''
    frase_nova=list(frase)
    i=0
    maiuscula=[]
    while i<len(frase):
        if frase_nova[i] in "çbcdfghjklmnpqrstvxwyz":
            maiuscula.append(frase_nova[i].upper())
            i+=1
    return maiuscula