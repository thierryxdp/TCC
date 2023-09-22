def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiou':
            str.upper(frase[i])
        i=i+1
        return i