def uppCons(frase):
    x=0
    y=frase[x]
    while y in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        return y
    x=x+1
    return y