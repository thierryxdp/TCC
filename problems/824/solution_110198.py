def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiou':
            frase[i]= frase[i].lower()
        if frase[i] in 'bcdfgh':
            frase[i]= frase[i].upper()
        i=i+1

    return frase