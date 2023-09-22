def uppCons(frase):
    str.upper(frase)
    frase = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] in 'AEIOU':
            frase[i] = str.lower(frase[i])
        i+=1
    return frase