def uppCons(t):
    s=''
    i=0
    while i < len(t):
        i += 1
        if t[i].lower() not in ('aeiou'):
            s += t[i].upper()
        else:
            s += t[i]
    return s