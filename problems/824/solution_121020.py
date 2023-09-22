def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            frase.upper(frase[i])
        i=i+1
    return frase