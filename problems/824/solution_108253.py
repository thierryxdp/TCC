def uppCons(frase):
    ''' '''
    c = 0
    CONS = ''
    
    while c < len(frase):
        if frase[c] in 'bcçdfghjklmnpqrstwxyzv':
            CONS=CONS+str.upper(frase[c])
        else:
            CONS=CONS + frase[c]
        c=c+1
         
    return CONS