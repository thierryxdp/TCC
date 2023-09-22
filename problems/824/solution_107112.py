def uppCons(frase):
    s = ''
    while x in frase:
        if x in 'bcdfghjklmnpqrstvxwyz':
            s=s+x.upper() 
        else: 
            s=s+x
    return s