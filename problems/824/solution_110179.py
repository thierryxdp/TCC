def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiouAEIOU':
            frase[i]=frase
        if frase[i] not in 'aeiouAEIOU':
            frase[i]=frase[i].upper()
        i=i+1
            
    return resultado