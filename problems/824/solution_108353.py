def uppCons(frase):
    i=o
    frasemscl=''
    while i<len(frase):
        if frase[i]!='aeiouAEIOU':
            frasemscl=frasemscl+str.lower(frase[i])
        else:
            frasemscl=frasemscl+str(frase[1])
    return frasemscl