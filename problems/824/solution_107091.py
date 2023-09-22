def uppCons(frase):
    x=0
    y=frase[x]
    while y in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        frase[x]=str.upper(frase[x])
        x=x+1
    
    return frase[x]