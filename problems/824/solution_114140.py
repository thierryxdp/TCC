def uppCons(frase):
    frase_volta = ''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXYZ':
            return str.upper(frase[i])
        frase_volta = frase_volta + frase[i]
        i = i + 1
    return frase_volta