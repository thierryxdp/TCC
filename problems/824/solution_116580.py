def uppCons(frase):
    s = ''
    for i in frase:
        if i in 'bcdfghjklmnpqrstvxwyz':
            s += i.upper()
        else:
            s += i
    return s