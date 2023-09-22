def uppCons(frase):
    i=0
    while i<len(frase):
        i=i+1
        if frase[i] not in 'AEIOUaeiou':
            return str.upper(frase[i])
    else:
            return frase[i]