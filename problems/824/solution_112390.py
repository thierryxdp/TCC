def uppCons(frase):
    i = 0
    while i <= len(frase):
        if frase[i] == 'aeiou':
            str.upper(frase[i])
        i+=1
    return frase