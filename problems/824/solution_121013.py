def uppCons(frase):
    b = 0
    fraseFinal= ' '
    while b < len(frase):
        a=frase[a]
        if a in 'bcdfghjklmnpqrstvwxyz':
            a=str.upper(a)
        fraseFinal=fraseFinal + a
        b= b + 1
    return fraseFinal