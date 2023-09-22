def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            frase.replace((frase[i]),(frase[1]).upper())
        i = i + 1
    return frase