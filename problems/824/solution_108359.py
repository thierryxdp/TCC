def uppCons(frase):
    i=0
    frasemscl=[str.split(frase)]
    while i<len(frase):
        if frase[i]!='aeiouAEIOU':
            frasemscl=frase.replace(frase[i],str.upper(frase[i]))
        else:
            frasemscl=frasemscl+str(frase[1])
    i=i+1
    return ' '.join(frasemscl)