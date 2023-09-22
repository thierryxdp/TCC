def conta_frases (x):
    r = 0
    pf= 0
    e = 0
    i = 0
    if "..." in x:
        r = str.count (x, "...")
    if "." in x:
        pf = str.count (x, ".") - 3*r
    if "!" in x: 
        e = str.count (x, "!")
    if "?" in x:
        i = str.count (x, "?")
    return r + pf + e + i