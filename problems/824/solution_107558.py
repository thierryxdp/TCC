def uppCons(frase):
    texto=0
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=str.upper(frase[i])
        if frase[i] in 'aeiou':
            texto=str.lower(frase[i])
        i=i+1
    return texto