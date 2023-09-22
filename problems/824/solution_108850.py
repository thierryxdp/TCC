def uppCons(frase):
    c=0
    f=' '
    while c<len(frase):
        crc=frase[c]
        if frase[c] in 'bcdfghjklmnpqrstvwxyz':
            frase[c] = str.upper(crc)
        f=f+crc
    return f