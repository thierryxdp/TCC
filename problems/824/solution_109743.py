def uppCons(frase):
    str.upper(frase)
    i = 0 
    
    while i < len(frase):
        if frase[i] in 'AEIOU':
            str.lower(frase[i])
        i+=1
    return frase