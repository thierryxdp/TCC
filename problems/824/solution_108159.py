def uppCons(frase):
    ''' '''
    c = 0
    CONS = ''
    while c < len(frase):
        if frase[c] not in 'AEIOUaeiou':
            CONS=str.upper(CONS+frase[c])
        c=c+1
        if frase[c] in 'AEIOUaeiou':
            CONS=str.lower(CONS+frase[c])
        c=c+1
    return CONS