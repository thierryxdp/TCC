def conta_frases (x):
    y = x.replace("...","*")
    p = y.replace("!","*")
    k = p.replace(".","*")
    t = k.replace("?","*")
    o = str.split(t,"*")
    d = len(o)-1
    return d