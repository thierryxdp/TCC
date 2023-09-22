def uppCons(frase):
    i=0
    frasemscl=[]
    while i<len(frase):
        str.split(frase)
        if frase[i]!='aeiouAEIOU':
            frasemscl=frasemscl+str.upper(frase[i])
        else:
            frasemscl=frasemscl+str(frase[1])
    i=i+1
    return ' '.join(frasemscl)