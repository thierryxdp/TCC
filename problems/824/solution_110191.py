def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiou':
            frase[i]= frase.upper(frase[i])
        if frase[i] not in 'aeiou':
            frase[i]= frase.upper(frase[i])
        i=i+1
            
    return frase