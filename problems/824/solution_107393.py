def uppCons(frase):
    resultado= str.upper(frase)
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwyz' and frase[0]:
            return resultado
        if frase[i] in 'aeiou':
            return str.lower(frase)
    i=i+1
    return resultado