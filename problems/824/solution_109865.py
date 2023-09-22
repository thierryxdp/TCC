def uppCons(frase):
    y= lambda x: x.upper() if x in 'bcçdfghjklmnpqrstvwxyz' else x
    s=list(map(y,frase))
    s=''.join(s)
    return s