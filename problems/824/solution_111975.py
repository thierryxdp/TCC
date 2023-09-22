def uppCons(texto):
   
    i=0
    frase=''
    while i<len(texto):
        if texto[i] in 'bcdfghjklmnpqrstvxywz':
            frase = str.upper(frase) + texto[i] 
        elif texto[i] in 'aeiou':
            frase = frase + texto[i]
        i=i+1
    return frase