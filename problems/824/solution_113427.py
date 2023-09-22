def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxy':
            maiuscula=str.upper(frase[i])
            frase=str.replace(frase,frase[i],maiuscula)
        i=i+1
    return frase