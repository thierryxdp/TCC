uppCons(frase):
    new=''
    t=0
    while t<len(frase):
        cons=frase[t]
        if cons in 'bcdfgjklmnpqrstwxyz':
            cons=str.upper(cons)
        new+=cons
        t+=1
    return new