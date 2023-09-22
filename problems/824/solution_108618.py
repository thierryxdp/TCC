def uppCons(frase):
    c=0
    f=' '
    while c<len(frase):
        crc=frase[c]
        if crc in 'bcdfghjklmnpqrstvwxyz':
            crc = str.upper(crc)
        f=f+crc
    return f