def uppCons(frase):
    i=0
    result=1
    while i<len(frase):
        if frase[i] not in 'aeiou' and frase[0]:
            return str.upper(frase)
        if frase[i] in 'aeiou':
            return str.lower(frase)
    i=i+1
    return frase