def uppCons(frase):
    s = ''
    x=0
    while frase[x] in frase:
        if frase[x] in 'bcdfghjklmnpqrstvxwyz':
            s=s+frase[x].upper() 
        else: 
            s=s+frase[x]
        x=x+1
    return s