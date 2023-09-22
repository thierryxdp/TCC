def uppCons(frase):
    s = ''
    x=0
    while x in frase:
        if x in 'bcdfghjklmnpqrstvxwyz':
            s=s+x.upper() 
        else: 
            s=s+x
        x=x+1
    return s