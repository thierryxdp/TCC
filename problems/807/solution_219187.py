def conta_frases (x):
    y = x.replace("...","@")
    p = y.replace("!","@")
    k = p.replace(".","@")
    t = k.replace("?","@")
    o = str.split(t,"@")
    k = str.strip(o)
    return len(k)-1