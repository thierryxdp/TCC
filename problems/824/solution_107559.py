def uppCons(frase):
    texto=0
    i=1
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' and frase[0]:
            texto=str.upper(frase[i])
        if frase[i] in 'aeiou':
            texto=str.lower(frase[i])
        i=i+1
    return texto