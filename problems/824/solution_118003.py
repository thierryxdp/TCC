def uppCons(frase):
    ''' '''
    i=0
    frase_nova=list(frase)
    maiuscula=''
    while i<len(frase):
        if frase_nova in "çbcdfghjklmnpqrstvxwyz":
            maiuscula.append(frase_nova[i].upper())
        i+=1
    return maiuscula