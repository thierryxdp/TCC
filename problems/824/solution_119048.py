def eh_cons(x):
    return x not in ("a", "e", "i", "o", "u")

def uppCons(s):
    r = []
    for e in s:
        if eh_cons(e):
            r.append(e.upper())
        else:
            r.append(e)
            
    return str.join(" ", r)