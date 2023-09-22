def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiouAEIOU':
            frase[i]=frase[i]
        if frase[i] not in 'aeiouAEIOU':
            frase[i]=frase.upper(frase[i])
        i=i+1
            
    return resultado