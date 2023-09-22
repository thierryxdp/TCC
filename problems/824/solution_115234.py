def uppCons(frase):
    i = 0 
    Nfrase = ''
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            Nfrase = frase[i]
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            Nfrase = str.upper(frase[i])
        i = i + 1 
    return Nfrase