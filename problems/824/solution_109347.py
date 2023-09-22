def uppCons(frase):
    frasefinal=''
    x=str.split(frase)
    i=0
    while i < len(x):
        if x[i] not in 'AEIOUaeiou':
            frasefinal += str.upper(frase[i])
        if x[i] in 'AEIOUaeiou':
            frasefinal += frase[i]
        i=i+1
    return str.join(' ',frasefinal)