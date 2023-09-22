def uppCons(frase):
    i=0
    while i<len(frase):
        frase[i] not in 'bcdfghjklmnpqrstvxwyz':
        str.upper(frase[i])
        i=i+1
    return frase