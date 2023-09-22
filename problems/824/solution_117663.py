def uppCons(frase):
    ''''''
    i = 0
    c = ''
    while i < len(frase):
        if frase[i] in 'BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz':
            c = c + str.upper(frase[i])
            i = i + 1
        else:
            c = c + frase [i]
            i = i + 1
    return c