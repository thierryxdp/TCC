def uppCons(frase):
    frasefinal=''
    i=0
    while i < len(frase):
        if frase[i] in 'AEIOUaeiouãõáéíúê':
            frasefinal += frase[i]
        if frase[i] not in 'AEIOUaeiouãõáéíúê':
            frasefinal += str.upper(frase[i])
        i=i+1
    return frasefinal