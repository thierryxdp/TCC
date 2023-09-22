def uppCons(frase):
    str.upper(frase)
    novafrase = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] in 'AEIOU':
            novafrase+= str.lower(frase[i])
        i+=1
    return novafrase