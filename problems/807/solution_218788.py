def conta_frases(F):
    x0 = str.split(F,('. '))
    x1 = str.split(x0,('! '))
    x2 = str.split(x1,('? '))
    x3 = str.split(x2,('...'))
    return len(x3)