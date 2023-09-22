def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            i=i+1
            return str.lower(frase)
        else:
            return str.upper(frase)