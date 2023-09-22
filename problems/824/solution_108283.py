def uppCons(frase):
    i = 0
    fraseFinal = ''
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            fraseFinal = fraseFinal + frase[i]
        i = i + 1
    return (fraseFinal).upper()