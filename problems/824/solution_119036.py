def eh_cons(x):
    return x not in ("a", "e", "i", "o", "u")

def uppCons(s):
    r = []
    for e in s:
        if eh_cons(e):
            r.append(e.upped())
        else:
            r.append(e)
    retur str.join("", r)