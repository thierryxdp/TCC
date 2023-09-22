def uppCons(frase):
    frase_volta = ''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcdefghjklmnpqrstvwxyz':
            str.upper(frase[i])
        i = i + 1
    return frase