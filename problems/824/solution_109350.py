def uppCons(frase):
    frasefinal=''
    i=0
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            frasefinal += frase[i]
        if frase[i] not in 'AEIOUaeiouãéíúõê':
            frasefinal += str.upper(frase[i])
        i=i+1
    return frasefinal