def uppCons(frase):
    frasenew = ''
    x = 0
    i = 0
    while len(frase) > x:
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frasenew += frase[i].upper()
        else:
            frasenew += frase[i]
        x += 1
        i += 1
    return frasenew