def uppCons(t):
    i = 0
    cons = ''
    while i < len (t):
        if (t[i] in 'bcdfghjklmnpqrstxyz'):
            cons = str.upper(cons) + t[i]
        i = i + 1
    return cons