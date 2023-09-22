def uppCons(frase):
    u=list(frase)
    for e in u:
        if e in 'aeiou':
            str.upper(u)
    return u