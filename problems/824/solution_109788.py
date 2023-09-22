def uppCons(frase):
    i=0
    x=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            x=x+(frase[i].upper())
        i=i+1        
    return x