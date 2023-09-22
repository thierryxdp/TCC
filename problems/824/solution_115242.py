def uppCons(frase):
    i = 0 
    Nfrase = ''
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            Nfrase = Nfrase + frase[i]
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            Nfrase = Nfrase + str.upper(frase[i])
        else:
            Nfrase = Nfrase + frase[i]
        i = i + 1 
    return Nfrase