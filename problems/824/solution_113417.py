def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxy':
            maiucula=str.upper(frase[i])
            str.replace(frase,frase[i],maiuscula)
        i=i+1
    return frase