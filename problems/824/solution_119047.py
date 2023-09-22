def eh_cons(x):
    return x not in ("a", "e", "i", "o", "u", "é", "í", "ú", "ó", "á", "à", "ê", "ô")

def uppCons(s):
    r = []
    for e in s:
        if eh_cons(e):
            r.append(e.upper())
        else:
            r.append(e)
            
    return str.join(" ", r)