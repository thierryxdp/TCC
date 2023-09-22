def conta_frases (x):
    y = x.replace("...","@")
    p = y.replace("!","@")
    k = p.replace(".","@")
    t = k.replace("?","@")
    t = str.split(t,"@")
    o = str.strip(t)
    return len(o)-1