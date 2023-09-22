def uppCons(frase):
    i = 0
    frasef = ''
    while i<(len(frase)-1):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frasef + str.upper(frase[i])
        else:
            frasef + frase[i]
        i += 1
    return frasef