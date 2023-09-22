def consoante(s):
    if s == 'a':
        return True
    elif s == 'e':
        return True
    elif s == 'i':
        return True
    elif s == 'o':
        return True
    elif s == 'u':
        return True
def uppCons(s):
    r = list(s)
    for e in r:
        if consoante(e):
            str.upper(e)
    str.join(r)
    return r