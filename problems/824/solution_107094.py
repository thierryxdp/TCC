def uppCons(frase):
    x=0
    while x<len(frase):
        if frase[x] in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            return str.upper(frase[x])
        else:
            return frase[x]
        x=x+1
    return frase