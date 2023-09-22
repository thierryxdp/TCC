def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            return str.upper(frase[i])
        i=i+1
        else:
            return frase[i]