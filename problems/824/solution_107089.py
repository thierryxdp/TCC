def uppCons(frase):
    x=0
    y=frase[x]
    while y in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        return str.upper(frase[x])
    x=x+1
    return y