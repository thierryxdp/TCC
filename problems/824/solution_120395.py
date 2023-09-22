def eh_cons(x):
    return x not in ("a", "e", "i", "o", "u", "à", "á", "â", "ã", "é", "ê","í", "ó", "ô", "õ", "ú")

def uppCons(s):
    r = []
    for e in s:
        if eh_cons(e):
            r.append(e.upper())
        else:
            r.append(e)
            
    return str.join("", r)