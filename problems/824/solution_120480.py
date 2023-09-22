def uppCons(t):
    s=''
    i=0
    while i < len(t):
        if t[i].lower() not in ('aeiou'):
            s += t[i].upper()
        else:
            s += t[i]
        i += 1
    return s