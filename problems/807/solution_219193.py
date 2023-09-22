def conta_frases (x):
    y = x.replace("...","*")
    p = y.replace("!","*")
    k = p.replace(".","*")
    t = k.replace("?","*")
    o = str.split(t,"*")
    f = str.strip(o)
    d = len(f)-1
    return d